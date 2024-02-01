from django.urls import path, include
from peststagram.accounts.views import signup_user, signin_user, details_user, edit_user, delete_user

urlpatterns = [
    path('sign_up/', signup_user, name="sign_up"),
    path('sign_in/', signin_user, name="sign_in"),
    path('profile/<int:pk>/', include([
        path('', details_user, name="details_user"),
        path('edit/', edit_user, name="edit_user"),
        path('delete/', delete_user, name="delete_user"),
    ]))
]