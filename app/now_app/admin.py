from django.contrib import admin

from now_app.models import ComMuseumList, NowLocality, ComSpecies, RefReference

class NowLocalityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["loc_name"]}),
        ("Locality", {"fields": ["country", "state", "county", "loc_detail", "site_area", "gen_loc", "plate", ]}),
    ]

admin.site.register(ComMuseumList)
admin.site.register(ComSpecies)
admin.site.register(NowLocality, NowLocalityAdmin)
admin.site.register(RefReference)
