# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *

# Create your models here.
class Ubicacion(models.Model):
	
	municipio=models.CharField(max_length=30)

	def __str__(self):
		return '{} '.format(self.idVisitante)

		
class Encuesta(models.Model):

	admin=models.OneToOneField(User)
	nombre=models.CharField(max_length=50)
	estado=models.BooleanField()
	numPreguntas=models.IntegerField()
	poblacion=models.IntegerField()
	tamMuestra=models.IntegerField()

	def __str__(self):
		return '{} '.format(self.idEncuesta)


class Visitante(models.Model):
	
	Encuesta=models.ForeignKey(Encuesta,on_delete=models.CASCADE)
	ip=models.CharField(max_length=100)
	ubicacion=models.OneToOneField(Ubicacion, on_delete=models.CASCADE)


class Pregunta(models.Model):
	
	visitante=models.ForeignKey(Visitante, on_delete=models.CASCADE )
	encuesta=models.ForeignKey(Encuesta,on_delete=models.CASCADE)
	enunciado=models.CharField(max_length=150)
	tipo=models.CharField(max_length=15)
	numRespuestas=models.IntegerField()

	def __str__(self):
		return '{} '.format(self.idPregunta)

class Respuesta(models.Model):

	pregunta=models.ForeignKey(Pregunta, on_delete=models.CASCADE)
	enunciadoRes=models.CharField(max_length=80)
	cantidad=models.IntegerField()
	

	def __str__(self):
		return '{} '.format(self.idRespuesta)



