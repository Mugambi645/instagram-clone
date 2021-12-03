from django.urls import path
from . import views
app_name = "homepage"
urlpatterns = [
    path("index/", views.index, name="index"),
]