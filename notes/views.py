from .models import Notes
from rest_framework import viewsets, permissions
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):

    queryset = Notes.objects.all()

    serializer_class = NoteSerializer

    permission_classes = [permissions.AllowAny]
