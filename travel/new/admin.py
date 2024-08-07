from django.contrib import admin
from new.models import Contact, Newsletter



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'created_date',)
    list_filter = ('email',)
    search_fields = ('name', 'message')
    date_hierarchy = 'created_date'
    

admin.site.register(Newsletter)