"""
URL configuration for wikimedia_capx project.

"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("bug.urls")),
    path("bug/", include("bug.urls")),
    path("admin/", admin.site.urls),
]