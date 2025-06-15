from django.urls import path
from car_service.views import car_service_home_page, parts


urlpatterns = [
    path('', car_service_home_page),
    path('parts/<int:part_id>/', parts),
]
