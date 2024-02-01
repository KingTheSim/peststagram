from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def signup_user(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/register-page.html")


def signin_user(request: HttpRequest) -> HttpResponse:
    return render(request, "accounts/login-page.html")


def details_user(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, "accounts/profile-details-page.html")


def edit_user(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, "accounts/profile-edit-page.html")


def delete_user(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, "accounts/profile-delete-page.html")
