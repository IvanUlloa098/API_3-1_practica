from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
import json
from .models import contactos
from .serializers import ContactosSerializer

class ContactosViewSet(viewsets.ModelViewSet):
  queryset = contactos.objects.all()
  serializer_class = ContactosSerializer

class crearContacto(APIView):
    def post(self, request):
      nombre = request.data.get('nombre')
      numero = request.data.get('numero')
    
      if nombre != "" and numero != "":
        
        with connection.cursor() as cursor:
          
          query = '''INSERT INTO contactos (nombre,numero) 
                      VALUES (%s, %s)
                  '''
          cursor.execute(query,[nombre, numero])
         
        return Response({"status":"Datos guardados"},status=status.HTTP_200_OK) 
      else:
        return Response({"status": "datos no ingresados"}, status=status.HTTP_400_BAD_REQUEST)