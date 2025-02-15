from rest_framework import serializers
from .models import Portfolio, Artwork, Comment, Notification

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'name', 'user', 'created_at']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty or whitespace.")
        return value

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ['id', 'title', 'description', 'image_url', 'user', 'category', 'portfolio', 'created_at']

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title cannot be empty or whitespace.")
        return value

    def validate_image_url(self, value):
        if not value.strip():
            raise serializers.ValidationError("Image URL cannot be empty or whitespace.")
        return value

    def validate_category(self, value):
        if value and not value.strip():
            raise serializers.ValidationError("Category cannot be just whitespace.")
        return value

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'artwork', 'created_at']

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty or whitespace.")
        return value

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'message', 'user', 'is_read', 'created_at']

    def validate_message(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message cannot be empty or whitespace.")
        return value
