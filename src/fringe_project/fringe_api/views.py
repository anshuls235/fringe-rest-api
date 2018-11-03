from django.shortcuts import render
from rest_framework import viewsets

from . import models
from . import serializers
# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
