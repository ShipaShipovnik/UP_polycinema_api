from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PositionViewSet, TagDetailView, TagView, AsideView, RegisterView, ProfileView,CommentView,OrderView

router = DefaultRouter()
router.register('positions', PositionViewSet, basename='positions')

urlpatterns = [
    path("", include(router.urls)),
    path("tags/", TagView.as_view()),
    path("tags/<slug:tag_slug>/", TagDetailView.as_view()),
    path("aside/", AsideView.as_view()),
    path('register/', RegisterView.as_view()),
    path('profile/', ProfileView.as_view()),
    path("comments/", CommentView.as_view()),
    path("comments/<slug:position_slug>/", CommentView.as_view()),
    path("orders/", OrderView.as_view()),
    path("orders/<slug:position_slug>/", OrderView.as_view()),
]
