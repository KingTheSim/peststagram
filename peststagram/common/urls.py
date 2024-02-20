from django.urls import path
from peststagram.common.views import like_functionality, copy_link_to_clipboard, add_comment, IndexPageView

urlpatterns = [
    path('', IndexPageView.as_view(), name="home"),
    path('like/<int:photo_id>/', like_functionality, name="like"),
    path('share/<int:photo_id>/', copy_link_to_clipboard, name="share"),
    path('comment/<int:photo_id>/', add_comment, name="comment"),
]
