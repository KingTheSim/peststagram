from django.urls import path,include
from peststagram.pests.views import add_pest, details_pest, edit_pest, delete_pest

urlpatterns = [
    path('add/', add_pest, name="add_pest"),
    path('<str:username>/pest/<slug:pest_slug>/', include([
        path('', details_pest, name="details_pest"),
        path('edit/', edit_pest, name="edit_pest"),
        path('delete/', delete_pest, name="delete_pest"),
    ]))
]