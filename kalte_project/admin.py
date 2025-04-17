from django.contrib import admin
from .models import Users

@admin.register(Users)
class KalteProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    
