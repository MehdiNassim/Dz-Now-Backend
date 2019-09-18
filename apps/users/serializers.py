from rest_framework import serializers
from . import models


class ReaderSerializer(serializers.ModelSerializer):
    """A serializer for the readers objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'first_name', 'last_name')
