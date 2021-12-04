from django.urls import path
from . import views
app_name = "profileApp"
urlpatterns = [
       path('profile/', views.profile, name='profile'),
]