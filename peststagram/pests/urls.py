from django.urls import path, include
from peststagram.pests.views import AddPestView, DetailsPestView, EditPestView, DeletePestView

urlpatterns = [
    path('add/', AddPestView.as_view(), name="add_pest"),
    path('<str:username>/pest/<slug:slug>/', include([
        path('', DetailsPestView.as_view(), name="details_pest"),
        path('edit/', EditPestView.as_view(), name="edit_pest"),
        path('delete/', DeletePestView.as_view(), name="delete_pest"),
    ])),
]
