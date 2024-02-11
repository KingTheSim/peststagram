from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def add_pest(request: HttpRequest) -> HttpResponse:
    return render(request, "pests/pest_add_page.html")


def details_pest(request: HttpRequest, username: str, pest_slug: str) -> HttpResponse:
    return render(request, "pests/pest_details_page.html")


def edit_pest(request: HttpRequest, username: str, pest_slug: str) -> HttpResponse:
    return render(request, "pests/pest_edit_page.html")


def delete_pest(request: HttpRequest, username: str, pest_slug: str) -> HttpResponse:
    return render(request, "pests/pest_delete_page.html")
