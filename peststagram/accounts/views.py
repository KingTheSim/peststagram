from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def signup_user(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/register_page.html")


def signin_user(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/login_page.html")


def details_user(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, "accounts/profile_details_page.html")


def edit_user(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, "accounts/profile_edit_page.html")


def delete_user(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, "accounts/profile_delete_page.html")
