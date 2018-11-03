from rest_framework import serializers

from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    """A Serializer for UserProfile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'corporate_email',
        'name','phone_no','image','date_joined','last_login')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email = validated_data['email'],
            corporate_email = validated_data['corporate_email'],
            name = validated_data['name'],
            phone_no = validated_data['phone_no'],
            image = validated_data['image']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
