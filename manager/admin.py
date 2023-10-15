from django.contrib import admin
from .models import Password

@admin.register(Password)
class PasswordAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'length', 'value')
    list_filter = ('owner', 'length')
    search_fields = ('name', 'owner__username')

# Optionally, you can customize the PasswordAdmin class to fit your needs.
