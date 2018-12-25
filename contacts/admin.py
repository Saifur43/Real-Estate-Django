from django.contrib import admin
from .models import Contacts


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('email', 'name', 'listing')
    list_per_page = 20


admin.site.register(Contacts, ContactAdmin)
