from django.contrib import admin

from .models import Asmr


class AsmrAdmin(admin.ModelAdmin):
    list_display = ['name', 'info', 'genre']
    list_display_links = ['name']

admin.site.register(Asmr, AsmrAdmin)
# Register your models here.
