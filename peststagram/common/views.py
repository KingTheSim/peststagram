from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from peststagram.common.models import Like
from peststagram.photos.models import Photo


def index(request: HttpRequest) -> HttpResponse:
    all_photos = Photo.objects.all()

    context = {
        "all_photos": all_photos,
    }
    return render(request, "common/home_page.html", context=context)


def like_functionality(request: HttpRequest, photo_id: int) -> HttpResponse:
    try:
        photo = Photo.objects.get(id=photo_id)
        liked_photo = Like.objects.filter(to_photo_id=photo_id).first()

        if liked_photo:
            liked_photo.delete()
        else:
            like = Like(to_photo=photo)
            like.save()

        return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")

    except ObjectDoesNotExist:
        return redirect(request.META["HTTP_REFERER"])
