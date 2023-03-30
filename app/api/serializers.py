from rest_framework import serializers
from now_app import models as now_models

class MuseumSerializer(serializers.ModelSerializer):
	class Meta:
		model = now_models.ComMuseumList
		exclude = ('used_morph', 'used_now', 'used_gene')

class NowMuseumSerializer(serializers.ModelSerializer):
	class Meta:
		model = now_models.NowMuseum
		fields = ('__all__')

class LocalitySerializer(serializers.ModelSerializer):
	class Meta:
		model = now_models.NowLocality
		exclude = ()
