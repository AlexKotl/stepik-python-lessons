from django.conf.urls import url
from routing.views import simple_route

urlpatterns = [
    url(r'^simple_route/', simple_route)
]
