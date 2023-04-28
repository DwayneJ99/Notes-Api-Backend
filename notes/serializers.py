from .models import Notes
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class NoteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta: 
        model = Notes

        fields = ['id', 'title', 'note']

