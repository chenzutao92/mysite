from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^list/(?P<block_id>\d+)/$', views.article_list, name='article_list'),
    url(r'^detail/(?P<article_id>\d+)/$', views.article_detail, name='article_detail'),
    url(r'^list/(?P<block_id>\d+)/article_create/$', views.article_create, name='article_create'),
]