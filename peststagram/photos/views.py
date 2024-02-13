from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from peststagram.photos.forms import PhotoCreateForm, PhotoEditForm
from peststagram.photos.models import Photo


def add_photo(request: HttpRequest) -> HttpResponse:
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("home")

    else:
        context = {
            "form": form,
        }
        return render(request, "photos/photo_add_page.html", context)


def details_photo(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        photo = Photo.objects.get(pk=pk)
        likes = photo.like_set.all()
        comments = photo.comment_set.all()

        context = {
            "photo": photo,
            "likes": likes,
            "comments": comments,
        }
        return render(request, "photos/photo_details_page.html", context)

    except ObjectDoesNotExist:
        return redirect("home")


def edit_photo(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        photo = Photo.objects.get(pk=pk)
        form = PhotoEditForm(request.POST or None, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('details_photo', pk=pk)

        else:
            context = {
                "form": form,
                "photo": photo,
            }
            return render(request, "photos/photo_edit_page.html", context)

    except ObjectDoesNotExist:
        return redirect("home")


def delete_photo(request: HttpRequest, pk: int) -> HttpResponse:
    try:
        photo = Photo.objects.get(pk=pk)
        photo.delete()
        return redirect("home")

    except ObjectDoesNotExist:
        return redirect("home")