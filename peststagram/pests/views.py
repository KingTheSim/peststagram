from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def add_pest(request: HttpRequest) -> HttpResponse:
    return render(request, "pests/pest-add-page.html")


def details_pest(request: HttpRequest, username: str, pest_slug: str) -> HttpResponse:
    return render(request, "pests/pest-details-page.html")


def edit_pest(request: HttpRequest, username: str, pest_slug: str) -> HttpResponse:
    return render(request, "pests/pest-edit-page.html")


def delete_pest(request: HttpRequest, username: str, pest_slug: str) -> HttpResponse:
    return render(request, "pests/pest-delete-page.html")
