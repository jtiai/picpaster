from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.index, name='index'),
    url('^upload/$', views.file_upload, name='upload'),
    url('^picture/(?P<key>)/', views.full_picture, name='picture'),
]
