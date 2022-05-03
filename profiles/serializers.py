from .models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "id",
            "dob",
            "user",
            "course",
            "specialization",
            "enrolled_year",
            "current_year",
            "contact",
            "github",
            "linkedin",
            "url",
        ]
        read_only = "user"

    # custom create profile function
    def create(self, validated_data):
        profile = Profile(**validated_data)
        request = self.context.get("request")
        profile.user = request.user
        return profile
