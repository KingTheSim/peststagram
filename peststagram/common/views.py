from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from pyperclip import copy
from peststagram.common.models import Like
from peststagram.common.forms import CommentForm, SearchForm
from peststagram.photos.models import Photo


def index(request: HttpRequest) -> HttpResponse:
    all_photos = Photo.objects.all()
    comment_form = CommentForm()
    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        all_photos = all_photos.filter(
            tagged_pests__name__icontains=search_form.cleaned_data["pest_name"],
        )

    context = {
        "all_photos": all_photos,
        "comment_form": comment_form,
        "search_form": search_form,
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


def copy_link_to_clipboard(request: HttpRequest, photo_id: int) -> HttpResponse:
    copy(request.META["HTTP_HOST"] + resolve_url("details_photo", photo_id))
    return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")


def add_comment(request: HttpRequest, photo_id: int) -> HttpResponse:
    try:
        photo = Photo.objects.get(id=photo_id)
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.save()

        return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")

    except ObjectDoesNotExist:
        return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")