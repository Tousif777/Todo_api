from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *


class TodolistView(viewsets.ModelViewSet):
	queryset = Todolist.objects.all()
	serializer_class = TodolistSerializer