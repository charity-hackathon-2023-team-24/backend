from django.urls import path

from . import views

urlpatterns = [
    path("dummy_json", views.dummy_json, name="dummy_json"),
]
