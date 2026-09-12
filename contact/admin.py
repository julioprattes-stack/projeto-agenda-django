from django.contrib import admin

from .models import ContactModel

@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone',)
    ordering = ('id',)
    search_fields = ('id', 'firts_name',)
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name',