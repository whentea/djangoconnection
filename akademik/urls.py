from django.conf.urls import url
from akademik import views

app_name = "akademik"
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^create/$', views.create, name='create'),
    url('^show/$', views.show, name='show'),
    url('^delete/(?{<document_id>[a-z0-9]*)/$', views.delete, name='delete'),
]