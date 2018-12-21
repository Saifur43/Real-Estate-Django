from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'hire_date', 'is_mvp')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'hire_date')
    list_editable = ('is_mvp',)
    search_fields = ('id', 'name', 'phone', 'email', 'hire_date', 'is_mvp')
    list_per_page = 20


admin.site.register(Realtor, RealtorAdmin)
