from django.shortcuts import render, redirect, resolve_url
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
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

    photos_per_page = 1
    paginator = Paginator(all_photos, photos_per_page)
    page = request.GET.get("page")

    try:
        all_photos = paginator.page(page)
    except PageNotAnInteger:
        all_photos = paginator.page(1)
    except EmptyPage:
        all_photos = paginator.page(paginator.num_pages)

    context = {
        "all_photos": all_photos,
        "comment_form": comment_form,
        "search_form": search_form,
    }

    return render(request, "common/home_page.html", context=context)


class IndexPageView(ListView):
    model = Photo
    template_name = "common/home_page.html"
    context_object_name = "all_photos"
    paginate_by = 1

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        context["search_form"] = SearchForm()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pest_name = self.request.GET.get("pest_name")

        if pest_name:
            self.request.session["pest_name"] = pest_name
        else:
            self.request.session.pop("pest_name", None)

        pest_name_session = self.request.session.get("pest_name_session")

        if pest_name:
            queryset = queryset.filter(tagged_pests__name__icontains=pest_name)

        return queryset.order_by("date_of_publication")


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

    except Photo.DoesNotExist:
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

    except Photo.DoesNotExist:
        return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")