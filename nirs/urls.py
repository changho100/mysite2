from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.exe_search_html),
]