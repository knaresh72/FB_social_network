# api/serializers.py
from rest_framework import serializers
from .models import UserProfile, FriendRequest, Friendship

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'

class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = '__all__'
