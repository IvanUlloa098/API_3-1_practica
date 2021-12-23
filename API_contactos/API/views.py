from django.http.response import HttpResponse
from django.shortcuts import render

from rest_framework import serializers, viewsets
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

class listarContactos(APIView):
    def get(self, request):
      
        try:
            with connection.cursor() as cursor:
                query = '''SELECT *
                            FROM contactos c 
                        '''
                cursor.execute(query)
                
                registros = [dict((cursor.description[i][0], value) \
                            for i, value in enumerate(row)) for row in cursor.fetchall()]
                
                json_output = json.dumps([dict(ix) for ix in registros] )
                print(f"WE ARE HERE!!!!!!!!! {json_output}")
                #serializer = ContactosSerializer(json_output)

                return HttpResponse(json_output, content_type='application/json')
        except:    
            return Response({"status": "No encontrado"}, status=status.HTTP_404_NOT_FOUND)
        