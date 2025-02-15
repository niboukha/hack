from django.db import models
from django.contrib.auth.models import User  # Using Django's built-in User model

class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolios')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Artwork(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(max_length=500)  # Storing image as URL or file path
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='artworks')
    category = models.CharField(max_length=100, blank=True, null=True)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.SET_NULL, null=True, blank=True, related_name='artworks')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.artwork.title}'


class Notification(models.Model):
    message = models.TextField()
    # message_status = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Notification for {self.user.username} - Read: {self.is_read}'
