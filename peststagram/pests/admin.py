from django.contrib import admin
from peststagram.pests.models import Pest


@admin.register(Pest)
class PestAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
