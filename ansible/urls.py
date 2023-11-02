from django.urls import path

from . import views

app_name = 'ansible'

urlpatterns = [
    path('', views.vmware),
    path('exe_search_vmware/', views.exe_search_vmware),
    path('exceldown/', views.exceldown),
]