from django.contrib.auth.models import User

# from posts.serializers import PostSerializer
from profiles.serializers import ProfileSerializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

# Register serializer
class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = ('username','email','password','confirmpassword')
        # fields = ("username", "password", "first_name", "last_name")
        fields = ("username", "password", "email")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(  # type: ignore
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            # first_name=validated_data["first_name"],
            # last_name=validated_data["last_name"],
        )
        # user = User.objects.create_user( username=validated_data['username'],email = validated_data['email'] , password = validated_data['password'],confirmpassword = validated_data['confirmpassword'] )
        return user


# User serializer
class UserSerializer(ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = User
        fields = "__all__"


class ShortUserSerialize(ModelSerializer):
    profile_image = serializers.ImageField(source="profile.profile_image")

    class Meta:
        model = User
        fields = ["username", "id", "email", "profile_image"]
