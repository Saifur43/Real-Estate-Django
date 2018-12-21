from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'Price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'list_date', 'Price')
    list_editable = ('is_published',)
    search_fields = ('id', 'title', 'is_published', 'Price', 'list_date', 'realtor')
    list_per_page = 20
    ordering = ('id',)


admin.site.register(Listing, ListingAdmin)
