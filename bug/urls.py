from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_bugs, name="all_bugs"),
    path("add_bug", views.add_bug, name="add_bug"),
    path('bug_detail/<int:id>/', views.bug_detail, name='bug_detail')
]