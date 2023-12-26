# api/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)


class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='friend_requests_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='friend_requests_received', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, default='pending')  # pending, accepted, rejected
    created_at = models.DateTimeField(auto_now_add=True)


    def accept(self):
        self.status = 'accepted'
        self.save()

    def reject(self):
        self.status = 'rejected'
        self.save()

class Friendship(models.Model):
    user1 = models.ForeignKey(User, related_name='friendship_user1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='friendship_user2', on_delete=models.CASCADE)

    @classmethod
    def are_friends(cls, user1, user2):
        return cls.objects.filter((models.Q(user1=user1, user2=user2) | models.Q(user1=user2, user2=user1))).exists()


