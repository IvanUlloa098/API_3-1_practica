# serializers.py
from rest_framework import serializers
from .models import contactos

class ContactosSerializer(serializers.ModelSerializer):
  class Meta: 
        model = contactos
        fields = ('id', 'nombre', 'numero',)