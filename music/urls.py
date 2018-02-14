from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # /music/
    path('', views.index, name='index'),

    # /music/album_id
    # path('(?P<album_id>[0-9]+)/', views.detail, name='detail'),
    url(r'^(?P<album_id>[0-9]+)/$',views.detail, name='detail'),
]

