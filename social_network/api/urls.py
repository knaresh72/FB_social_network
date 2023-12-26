#api/urls.py

from django.urls import path
from .views import UserSearchAPIView, FriendRequestAPIView, FriendListAPIView, PendingFriendRequestAPIView, user_login

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('search/', UserSearchAPIView.as_view(), name='user-search'),
    path('friend-request/', FriendRequestAPIView.as_view(), name='friend-request'),
    path('friend-list/', FriendListAPIView.as_view(), name='friend-list'),
    path('pending-requests/', PendingFriendRequestAPIView.as_view(), name='pending-requests'),
]




