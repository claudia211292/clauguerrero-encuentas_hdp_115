# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Encuesta.models import *
from django.contrib.auth import authenticate,login
from django.contrib import messages

def login_view(request):

	if request.method == "POST":
		_usuario = request.POST.get('usuario')
		_pass = request.POST.get('password')
		user = authenticate(username=_usuario, password=_pass)

		if user is not None:
			login(request, user)
			return render(request,'Main/index.html') #Vista pendiente para redireccionar
		else:
			messages.add_message(request,messages.ERROR,"Error crendenciales incorrectas")

	return render(request, 'Main/index.html')

# Create your views here.

def index(request):
	return render(request,'Main/index.html',{})

@login_required(login_url='/')
def encuesta_crear(request):
	return render(request,'Main/editar_encuesta.html',{})

def encuesta_guardar(request):
	z=0.9 #Confiabilidad"""
	e=0.5 #Error"""
	sigma=0.5 #Desviación"""
	#admin=Administrador()
	#admin.idAdmin="hola"
	#admin.password="holahola"
	#admin.save()

	encuesta=Encuesta()
	encuesta.nombre = request.POST["nombreEncuesta"]
	encuesta.poblacion=int(request.POST["inpoblacion"])
	encuesta.estado=False
	encuesta.numPreguntas=0
	#calculo de la muestra
	m=int((encuesta.poblacion*sigma*sigma*z*z)/(e*(encuesta.poblacion-1)+(sigma*sigma*z*z)))
	encuesta.tamMuestra=m
	
	encuesta.save()
	return redirect("/")
