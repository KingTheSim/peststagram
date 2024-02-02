from django.db import models
from django.core.validators import MinLengthValidator

from peststagram.photos.validators import validate_photo_size
from peststagram.pests.models import Pest


class Photo(models.Model):
    MAX_NAME_LENGTH = 20

    MAX_DESCRIPTION_LENGTH = 300
    MIN_DESCRIPTION_LENGTH = 10

    MAX_LOCATION_LENGTH = 30

    name = models.CharField(max_length=MAX_NAME_LENGTH)
    picture = models.ImageField(upload_to="photos/", validators=(validate_photo_size,))
    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(MinLengthValidator(MIN_DESCRIPTION_LENGTH),),
        blank=True,
        null=True,
    )
    location = models.CharField(max_length=MAX_LOCATION_LENGTH, blank=True, null=True)
    tagged_pests = models.ManyToManyField(Pest, blank=True, related_name="tagged_pests")
    date_of_publication = models.DateField(auto_now_add=True)
    time_of_modification = models.DateTimeField(auto_now=True)
