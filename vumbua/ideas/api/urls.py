from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ideas.api import views as qv

router = DefaultRouter()
router.register("ideas", qv.IdeasViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("ideas/<slug:slug>/comments/", qv.CommentsCreateAPIView.as_view(), name="comment-list"),
    path("ideas/<slug:slug>/comment/", qv.CommentsListAPIView.as_view(), name="comment-create"),
    path("comments/<int:pk>/", qv.CommentsRUDAPIView.as_view(), name="comment-detail"),
    path("comments/<int:pk>/like/", qv.CommentLikeAPIView.as_view(), name="comment-like"),
]
