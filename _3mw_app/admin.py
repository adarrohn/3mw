from django.contrib import admin
from .models import Site


class SiteAdmin(admin.ModelAdmin):
    """
    Site List Display for the Admin
    """
    list_display = ('name',
                    'date',
                    'val_a',
                    'val_b')

# Bind the Models to the Admin
admin.site.register(Site, SiteAdmin)