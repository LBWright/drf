from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloApiView, HelloViewSet, UserProfileViewSet

router = DefaultRouter()
router.register("hello-viewset", HelloViewSet, base_name="hello-viewset")
router.register("profiles", UserProfileViewSet, base_name="profiles")

urlpatterns = [
    path("hello-view/", HelloApiView.as_view()),
    path("", include(router.urls)),
]

