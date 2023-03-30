from django.shortcuts import render, redirect
from rest_framework.settings import api_settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.routers import APIRootView
from django.http.response import HttpResponseRedirectBase
from rest_framework import status
from django.urls import reverse
from rest_framework import permissions
from django_filters.views import FilterMixin

from . import serializers as api_serializers
from now_app import models as now_models
from . import renderers as api_renderers
from . import filters as now_filters
from .utils.query_params import preserve_view_query_params
# Create your views here.

class BaseViewSet(viewsets.ModelViewSet, FilterMixin):
	permission_classes = [permissions.DjangoModelPermissions]

	class Meta:
		abstract = True

class RendererExtensions():
	# Defines helper functions used by the WebRenderer. Any viewset using WebRenderer
	# must inherit this class or define similar functions for the renderer to function
	# correctly.

	def get_template(self, context):
		# Called by renderer to determine which template to render
		return 'rest_framework/api.html'

	def modify_context(self, context):
		# Called by renderer allowing the renderer context to be modified
		# Use in conjunction with get_template to customize a viewset view
		return context

	class Meta:
		abstract = True

class WebViewExtensions(RendererExtensions):
	# Implements generic next/previous navigation within (filtered) listings as well as
	# URLs and functionality for implementing custom create/edit pages

	def primary_key_field(self, model=None):
		if model == None:
			model = type(self.get_object())

		for field in model._meta.get_fields():
			if hasattr(field, 'primary_key') and field.primary_key is True:
				return field.name

	def redirect_to_detail(self, request, pk):
		url = reverse(self.basename + '-detail', kwargs={'pk': pk})
		url = preserve_view_query_params(self, url, request)
		return redirect(url)

	@action(detail=False, methods=['GET', 'POST'], name='new')
	def new(self, request):
		if request.method == 'GET':
			return Response()

		response = self.create(request)
		return self.redirect_to_detail(request, response.data[self.primary_key_field()])

	@action(detail=True, methods=['GET', 'PUT'], name='edit')
	def edit(self, request, pk):
		if request.method == 'GET':
			instance = self.get_object()
			serializer = self.get_serializer(instance)
			return Response(serializer.data)

		response = self.update(request)
		return self.redirect_to_detail(request, pk)

	@action(detail=True, methods=['GET', 'POST'])
	def form_edit(self, request, pk=None):
		if request.method == 'GET':
			instance = self.get_object()
			serializer = self.get_serializer(instance)
			return Response(serializer.data)

		# Forms only support GET and POST methods. Because forms may include only a subset
		# of the fields, a partial update is performed so blank or missing fields aren't deleted
		# from the model instance.
		response = self.partial_update(request)
		return self.redirect_to_detail(request, pk)

	@action(detail=True, methods=['GET'])
	def next(self, request, pk):
		qs = self.filter_queryset(self.get_queryset())

		instance = self.get_object()
		model = type(instance)
		pk_field_name = primary_key_field(model)

		instance_index = (*qs,).index(instance)
		next_index = min(instance_index + 1, qs.count() - 1)
		next_instance_pk = getattr(qs[next_index], pk_field_name)

		url = reverse(self.basename + '-detail', kwargs={'pk': next_instance_pk})
		url = preserve_view_query_params(self, url, request)
		return redirect(url)

	@action(detail=True, methods=['GET'])
	def previous(self, request, pk):
		qs = self.filter_queryset(self.get_queryset())

		instance = self.get_object()
		model = type(instance)
		pk_field_name = primary_key_field(model)

		instance_index = (*qs,).index(instance)
		next_index = max(instance_index - 1, 0)
		next_instance_pk = getattr(qs[next_index], pk_field_name)

		url = reverse(self.basename + '-detail', kwargs={'pk': next_instance_pk})
		url = preserve_view_query_params(self, url, request)
		return redirect(url)

	def destroy(self, request, *args, **kwargs):
		# Implementation identical to DRF DestroyModelMixin but redirects to list instead of returning code 204
		instance = self.get_object()
		self.perform_destroy(instance)
		url = reverse(self.basename + '-list')
		url = preserve_view_query_params(self, url, request)
		return HttpResponseRedirectBase(url, status=status.HTTP_303_SEE_OTHER)

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

# Note: Inherit from WebViewExtension first so ModelViewSet destroy is correctly overridden by WebViewExtensions
class MuseumWebViewSet(WebViewExtensions, MuseumViewSet):
	renderer_classes = [api_renderers.WebRenderer]

	def get_template(self, context):
		match self.action:
			case 'retrieve':
				return 'museum_detail.html'
			case 'list':
				return 'museum_list.html'
			case 'new':
				return 'museum_create_form.html'
			case 'edit':
				return 'museum_edit_form.html'
			case 'form_edit':
				return 'generic_form.html'
			case _:
				return super().get_template(context)

	def modify_context(self, context):
		from now_app import forms
		match self.action:
			case 'form_edit':
				context['django_form'] = forms.ComMuseumForm(initial=context['data'])

		return context

class LocalityViewSet(BaseViewSet):
	serializer_class = api_serializers.LocalitySerializer
	queryset = serializer_class.Meta.model.objects.all()

class LocalityWebViewSet(WebViewExtensions, LocalityViewSet):
	renderer_classes = [api_renderers.WebRenderer]

	def get_template(self, context):
		match self.action:
			case 'retrieve':
				return 'locality_detail.html'
			case 'list':
				return 'locality_list.html'
			case 'form_edit':
				return 'generic_form.html'
			case _:
				return super().get_template(context)

	def modify_context(self, context):
		from now_app import forms as now_forms
		match self.action:
			case 'form_edit':
				context['django_form'] = now_forms.NowLocalityForm(initial=context['data'])

		return context

class HomeView(APIRootView, RendererExtensions):
	renderer_classes = [api_renderers.WebRenderer]

	def get_template(self, context):
		return 'home.html'
