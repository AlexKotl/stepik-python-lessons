from django.conf.urls import url
from routing.views import *

urlpatterns = [
    url(r'^simple_route/', simple_route),
    url(r'^slug_route/([0-9a-z\-_]{1,16})', slug_route)
]
