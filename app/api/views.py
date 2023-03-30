from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.routers import APIRootView
from rest_framework import permissions
from django_filters.views import FilterMixin

from . import serializers as api_serializers
from now_app import models as now_models
# Create your views here.

class BaseViewSet(viewsets.ModelViewSet, FilterMixin):
	permission_classes = [permissions.DjangoModelPermissions]

	class Meta:
		abstract = True

class MuseumViewSet(BaseViewSet):
	serializer_class = api_serializers.MuseumSerializer
	queryset = serializer_class.Meta.model.objects.all()

class HomeView(APIRootView):

	def get_template(self, context):
		return 'home.html'
