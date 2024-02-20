from django.db import models
from django.template.defaultfilters import slugify


class Pest(models.Model):
    MAX_NAME_LENGTH = 30

    name = models.CharField(max_length=MAX_NAME_LENGTH)
    photo = models.URLField()
    description = models.TextField()
    date_of_sight = models.DateField()
    slug = models.SlugField(unique=True, null=False, blank=True, editable=False)

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")

        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
