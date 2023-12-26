# api/views.py
from django.db.models import Q
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from .models import UserProfile, FriendRequest, Friendship
from .serializers import UserProfileSerializer, FriendRequestSerializer, FriendshipSerializer
from rest_framework.decorators import api_view, permission_classes


@api_view(['POST'])
@permission_classes([AllowAny])
def user_signup(request):
    serializer = UserProfileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([AllowAny])
def user_login(request):
    email = request.data.get('email', '')
    password = request.data.get('password', '')

    if email and password:
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)

    return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserSearchAPIView(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')
        return User.objects.filter(Q(username__icontains=search_query) | Q(userprofile__some_field__icontains=search_query)).exclude(id=self.request.user.id)[:10]

class FriendRequestAPIView(CreateAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        to_user = serializer.validated_data['to_user']
        from_user = self.request.user

        # Check if users are already friends
        if Friendship.are_friends(from_user, to_user):
            return Response({'detail': 'Users are already friends.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if friend request already sent
        if FriendRequest.objects.filter(from_user=from_user, to_user=to_user, status='pending').exists():
            return Response({'detail': 'Friend request already sent.'}, status=status.HTTP_400_BAD_REQUEST)

        # Check rate limit - allow up to 3 requests within a minute
        rate_limit_key = f'friend_request_limit:{from_user.id}'
        request_count = cache.get(rate_limit_key, 0)
        if request_count >= 3:
            return Response({'detail': 'You have reached the maximum limit of friend requests within a minute.'},
                            status=status.HTTP_429_TOO_MANY_REQUESTS)

        # If not rate-limited, proceed with creating the friend request
        serializer.save(from_user=from_user)

        # Update the rate limit count in the cache
        cache.set(rate_limit_key, request_count + 1, timeout=60)  # 60 seconds (1 minute)

class FriendListAPIView(generics.ListAPIView):
    serializer_class = FriendshipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Friendship.objects.filter(Q(user1=user) | Q(user2=user))

class PendingFriendRequestAPIView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(to_user=self.request.user, status='pending')


