from rest_framework import serializers
from . import models


class NotesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Notes
        fields = ('title', 'description', 'created_at', 'updated_at')