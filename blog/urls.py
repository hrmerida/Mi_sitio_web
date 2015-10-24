from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.listado_post),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detalle_post),
    url(r'^post/new/$', views.post_nuevo, name='post_nuevo'),
    url(r'^post/(?P<pk>[0-9]+)/editar/$', views.editar_post, name='editar_post'),
]
