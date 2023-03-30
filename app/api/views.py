from django.shortcuts import render
from rest_framework.settings import api_settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.routers import APIRootView
from rest_framework import permissions
from django_filters.views import FilterMixin

from . import serializers as api_serializers
from now_app import models as now_models
from . import filters as now_filters
# Create your views here.

class BaseViewSet(viewsets.ModelViewSet, FilterMixin):
	permission_classes = [permissions.DjangoModelPermissions]

	class Meta:
		abstract = True

class MuseumViewSet(BaseViewSet):
	# From viewset
	serializer_class = api_serializers.MuseumSerializer
	queryset = serializer_class.Meta.model.objects.all()

	# Modify per-viewset properties here

	# authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES
	# content_negotiation_class = api_settings.DEFAULT_CONTENT_NEGOTIATION_CLASS
	# metadata_class = api_settings.DEFAULT_METADATA_CLASS
	# parser_classes = api_settings.DEFAULT_PARSER_CLASSES
	# permission_classes = api_settings.DEFAULT_PERMISSION_CLASSES
	# throttle_classes = api_settings.DEFAULT_THROTTLE_CLASSES
	# versioning_class = api_settings.DEFAULT_VERSIONING_CLASS

	# Filtering
	filterset_class = now_filters.MuseumFilter
	# ordering_fields = '__all__'
	# ordering = ['id']

class LocalityViewSet(BaseViewSet):
	serializer_class = api_serializers.LocalitySerializer
	queryset = serializer_class.Meta.model.objects.all()

class HomeView(APIRootView):

	def get_template(self, context):
		return 'home.html'
