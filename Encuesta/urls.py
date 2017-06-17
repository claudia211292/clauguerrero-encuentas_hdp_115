from django.conf.urls import url
from Encuesta.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^editarencuesta/',encuesta_crear, name='encuesta_editar'),
    url (r'^encuesta/guardar',encuesta_guardar),
]
