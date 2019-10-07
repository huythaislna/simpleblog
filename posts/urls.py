from django.conf.urls import url
from .views import(
    home, detail, create, update
)

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^create/$', create, name='create'),
    url(r'^(?P<id>\d+)/edit/$', update, name='update'),
    url(r'^(?P<id>\d+)/$', detail, name='detail'),
]