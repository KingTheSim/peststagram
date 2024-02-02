from django.db import models

from peststagram.photos.models import Photo


class Comment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.TextField(max_length=MAX_TEXT_LENGTH)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
