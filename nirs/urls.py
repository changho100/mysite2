from django.urls import path
from . import views

urlpatterns = [
    path('', views.exe_search_html),
]