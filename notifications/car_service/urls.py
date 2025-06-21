from django.urls import path
from car_service.views import car_service_homepage

urlpatterns = [
    path("", car_service_homepage, name='car_service'),
]
