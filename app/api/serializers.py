from rest_framework import serializers
from now_app import models as now_models

class MuseumSerializer(serializers.ModelSerializer):
	class Meta:
		model = now_models.ComMuseumList
		exclude = ('used_morph', 'used_now', 'used_gene')
