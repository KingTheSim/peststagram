from django import forms
from peststagram.photos.models import Photo


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ["name", "picture", "description", "location", "tagged_pests"]


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ["picture", "date_created", "time_created"]
