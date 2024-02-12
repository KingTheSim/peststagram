from django.urls import path
from peststagram.common.views import index, like_functionality

urlpatterns = [
    path('', index, name="home"),
    path('like/<int:photo_id>/', like_functionality, name="like"),
]
