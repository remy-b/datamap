#DataMap main app url.py 


from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^home$', views.home, name = 'home'),
    url(r'^map$', views.map, name = 'map'),
    url(r'^api_send_data/(?P<uuid>\w{32})/temp(?P<tempeture>\w{4})/humi(?P<humidity>\w{4})/noise(?P<noise>\w{2})$',views.log_send_by_url),
]
