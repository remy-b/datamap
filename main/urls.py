"""DataMap main app url.py """

from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^home$', views.home, name = 'home'),
    url(r'^map$', views.map, name = 'map'),
    url(r'^api_send_data/(?P<uuid>\w{32})/temp(?P<tempeture>\w{4})/humi(?P<humidity>\w{4})/noise(?P<noise>\w{2})$',views.log_send_by_url),
]

"""
    url(r'^sensor_list$', views.sensor_list, name = 'sensor_list'),
    url(r'^sensor_token=(?P<token>\w{4})$', views.sensorcara),

    url(r'^logs_token:(?P<token>\w{4})$', views.logs_list),

    url(r'^log_id=(?P<id_log>\w{4})$', views.log_data),

    url(r'^hometest$', views.homeTest, name = 'hometest'),
    url(r'^add_sensor$', views.add_sensor, name = "add_sensor"),
    url(r'^log_form$', views.logs_form, name = "logs_form"),
"""
