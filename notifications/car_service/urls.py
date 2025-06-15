from django.urls import path
from car_service.views import car_service_home_page


urlpatterns = [
    path('', car_service_home_page),
]
