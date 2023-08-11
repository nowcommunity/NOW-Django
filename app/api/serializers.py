from rest_framework import serializers
from now_app import models as now_models

class ComPeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = now_models.ComPeople
        fields = ['initials', 'surname',]


class MuseumSerializer(serializers.ModelSerializer):
	class Meta:
		model = now_models.ComMuseumList
		exclude = ('used_morph', 'used_now', 'used_gene')


class NowMuseumSerializer(serializers.ModelSerializer):
	class Meta:
		model = now_models.NowMuseum
		fields = ('__all__')

class LocalityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = now_models.NowLocality
        fields = ['lid','loc_name', 'country', 'max_age', 'min_age']


class LocalitySerializer(serializers.ModelSerializer):
	museum = serializers.PrimaryKeyRelatedField(many=True, queryset=now_models.ComMuseumList.objects.all())

	class Meta:
		model = now_models.NowLocality
		exclude = ()


class RefJournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = now_models.RefJournal
        fields = ['journal_title',]


class RefReferenceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = now_models.RefReferenceType
        fields = ['ref_type',]


class RefAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = now_models.RefAuthors
        fields = ['author_surname',]


class SpeciesLocalitySerializer(serializers.ModelSerializer):
	locality = LocalitySerializer(source='lid', read_only=True)

	class Meta:
		model = now_models.NowLocalitySpecies
		fields = ('__all__')


class SpeciesUpdateSerializer(serializers.ModelSerializer):
	sau_coordinator = ComPeopleSerializer()
	sau_authorizer = ComPeopleSerializer()

	class Meta:
		model = now_models.NowSpeciesUpdate
		fields = ('__all__')


class SpeciesSerializer(serializers.ModelSerializer):
	species_locality = SpeciesLocalitySerializer(many=True, read_only=True)
	species_update = SpeciesUpdateSerializer(many=True, read_only=True)

	#https://docs.djangoproject.com/en/4.2/ref/models/instances/#django.db.models.Model.get_FOO_display
	locomo1_display = serializers.CharField(source='get_locomo1_display')
	locomo2_display = serializers.CharField(source='get_locomo2_display')
	locomo3_display = serializers.CharField(source='get_locomo3_display')

#	sau_coordinator = ComPeopleSerializer(read_only=True)
#	sau_authorizer = ComPeopleSerializer(read_only=True)

	class Meta:
		model = now_models.ComSpecies
		fields = ('__all__')


class NowSpeciesUpdateReferenceSerializer(serializers.ModelSerializer):
	species = SpeciesSerializer(many=True, read_only=True)
	class Meta:
		model = now_models.NowSpeciesUpdateReference
		fields = ['rid','suid','species']


class ReferenceSerializer(serializers.ModelSerializer):
	journal = RefJournalSerializer(read_only=True)  # Nested representation of RefJournal model
	ref_type = RefReferenceTypeSerializer(read_only=True)  # Nested representation of RefReferenceType model
	authors = RefAuthorsSerializer(many=True, read_only=True)
	first_author = serializers.SerializerMethodField()
	species_updates = NowSpeciesUpdateReferenceSerializer(many=True, read_only=True)

	def get_first_author(self, obj):
		first_author = obj.authors.first()
		if first_author:
			return first_author.author_surname
		return None

	class Meta:
		model = now_models.RefReference
		fields = ['rid','title_primary' ,'date_primary', 'title_secondary', 'journal', 'ref_type', 'authors','first_author','volume','start_page','end_page','species_updates',]

