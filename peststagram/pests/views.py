from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from peststagram.pests.models import Pest
from peststagram.pests.forms import PestAddForm, PestEditForm, PestDeleteForm


def add_pest(request: HttpRequest) -> HttpResponse:
    form = PestAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("details_user", pk=1)

    context = {
        "form": form,
    }
    return render(request, "pests/pest_add_page.html", context=context)


def details_pest(request: HttpRequest, username: str, pest_slug: str) -> HttpResponse:
    try:
        pest = Pest.objects.get(slug=pest_slug)
        all_photos = pest.tagged_pests.all()
        context = {
            "pest": pest,
            "all_photos": all_photos,
        }
        return render(request, "pests/pest_details_page.html", context=context)

    except ObjectDoesNotExist:
        return redirect(request.META["HTTP_REFERER"])


def edit_pest(request: HttpRequest, username: str, pest_slug: str) -> HttpResponse:
    try:
        pest = Pest.objects.get(slug=pest_slug)
        form = PestEditForm(request.POST or None, instance=pest)
        if form.is_valid():
            form.save()
            redirect("details_user", username=username, pest_slug=pest_slug)

        else:
            context = {
                "form": form,
                "username": username,
                "pest_slug": pest_slug,
            }
            return render(request, "pests/pest_edit_page.html", context)

    except ObjectDoesNotExist:
        return redirect(request.META["HTTP_REFERER"])


def delete_pest(request: HttpRequest, username: str, pest_slug: str) -> HttpResponse:
    try:
        pest = Pest.objects.get(slug=pest_slug)
        form = PestDeleteForm(request.POST or None, instance=pest)
        if request.method == "POST":
            form.save()
            return redirect("home")

        else:
            context = {
                "form": form,
                "username": username,
                "pest": pest,
            }
        return render(request, "pests/pest_delete_page.html", context=context)

    except ObjectDoesNotExist:
        return redirect(request.META["HTTP_REFERER"])
