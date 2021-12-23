from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'contactos', ContactosViewSet)

urlpatterns = [
    path('api/allAPI/', include(router.urls)),
    path('api/crearcontacto/', crearContacto.as_view()),
    path('api/listarcontactos/', listarContactos.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]