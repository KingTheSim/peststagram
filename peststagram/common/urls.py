from django.urls import path
from peststagram.common.views import index

urlpatterns = [
    path('', index, name="home"),
]
