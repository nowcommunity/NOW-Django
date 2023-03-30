import django_filters as filters
from now_app import models

class MuseumFilter(filters.FilterSet):
	museum = filters.CharFilter(lookup_expr='icontains')
	institution = filters.CharFilter(lookup_expr='icontains')
	country = filters.CharFilter(lookup_expr='icontains')

	order = filters.OrderingFilter(fields=('museum', 'institution', 'id'))

	class Meta:
		model = models.ComMuseumList
		fields = ['museum', 'institution', 'country']
