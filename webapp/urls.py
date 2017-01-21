from django.conf.urls import url
from . import views

app_name = 'webapp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.blog, name='post'),
    url(r'^contact/$',views.contact, name="contact"),
    url(r'^contact/send$',views.send, name="send"),
    url(r'^blog/(?P<number>[0-9]+)/$', views.detail, name='detail'),
    url(r'^blog/(?P<number>[0-9]+)/comment$', views.comment, name='comment'),
]
