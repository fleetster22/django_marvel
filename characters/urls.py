from django.urls import path
from .views import character_list

urlpatterns = [path("", character_list, name="home")]
