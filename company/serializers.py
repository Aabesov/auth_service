from rest_framework import serializers

from accounts.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source="user.email")
    full_name = serializers.CharField(source="user.full_name")

    class Meta:
        model = Profile
        fields = ("email", "full_name", "salary",
                  "image", "department", "level")
