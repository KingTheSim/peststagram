from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from peststagram.photos.models import Photo


def index(request: HttpRequest) -> HttpResponse:
    all_photos = Photo.objects.all()

    context = {
        "all_photos": all_photos,
    }
    return render(request, "common/home_page.html", context=context)
