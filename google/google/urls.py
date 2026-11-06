from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect("/youtube/home/")),
    path("google_photos/", include("google_photos.urls")),
    path("google_maps/", include("google_maps.urls")),
    path("youtube/", include("youtube.urls")),
    path('admin/', admin.site.urls),
]