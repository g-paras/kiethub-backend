from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='author.user.username')
    profile_image = serializers.ImageField(source='author.profile_image', read_only=True)
    class Meta:
        model = Post
        fields = '__all__'