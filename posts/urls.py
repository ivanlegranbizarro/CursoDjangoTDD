from django.urls import path

from . import views

app_name = "posts"

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/<str:pk>/", views.detail, name="detail"),
]
