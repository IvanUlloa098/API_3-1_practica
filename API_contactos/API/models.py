from django.db import models

# Create your models here.
class contactos(models.Model): 
    id = models.AutoField(primary_key=True, null= False)
    nombre = models.CharField(max_length=255, blank= False, null= False)
    numero = models.CharField(max_length=255, blank= False, null= False)
    
    