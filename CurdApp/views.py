from rest_framework import viewsets
from . import models
from . import serializers


class NotesView(viewsets.ModelViewSet):
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NotesSerializer