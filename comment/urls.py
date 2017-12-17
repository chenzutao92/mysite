from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^comment/create/$', views.comment,name="comment"),
]