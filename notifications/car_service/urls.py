from django.urls import path
from car_service.views import homepage_view


# Пространство имён приложения
app_name = "car"

urlpatterns = [
    # URL: /car-service/parts/
    path("", homepage_view, name="homepage"),
]
