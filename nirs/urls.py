from django.urls import path
from . import views

urlpatterns = [
    path('', views.vmware),
    path('nirs/exe_search_vmware', views.exe_search_vmware),
]