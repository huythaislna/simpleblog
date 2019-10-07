from django.conf.urls import url
from .views import(
    home, detail, create, update, topic
)

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^topics/(?P<slug>\w+)/$', topic, name='topic'),
    url(r'^create/$', create, name='create'),
    url(r'^(?P<slug>[\w-]+)/edit/$', update, name='update'),
    url(r'^(?P<slug>[\w-]+)/$', detail, name='detail'),
]