from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def add_photo(request: HttpRequest) -> HttpResponse:
    return render(request, "photos/photo_add_page.html")


def details_photo(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, "photos/photo_details_page.html")


def edit_photo(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, "photos/photo_edit_page.html")
