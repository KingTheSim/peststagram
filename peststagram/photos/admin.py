from django.contrib import admin
from peststagram.photos.models import Photo
from peststagram.pests.models import Pest


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date_of_publication", "time_of_modification", "get_tagged_pests")

    @staticmethod
    def get_tagged_pests(obj: Pest) -> str:
        return ", ".join(pet.name for pet in obj.tagged_pests.all())
