from django.contrib import admin
from .models import Site, Entry


class SiteAdmin(admin.ModelAdmin):
    """
    Site List Display for the Admin
    """
    list_display = ('name',)


class EntryAdmin(admin.ModelAdmin):
    """
    Entry List Display for the Admin
    """
    list_display = ('site',
                    'date',
                    'val_a',
                    'val_b')

# Bind the Models to the Admin
admin.site.register(Site, SiteAdmin)
admin.site.register(Entry, EntryAdmin)