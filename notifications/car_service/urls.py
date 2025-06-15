from django.urls import path
from car_service.views import (
    car_service_home_page,
    parts_by_int,
    parts_by_slug,
)


urlpatterns = [
    path("", car_service_home_page),
    path("parts-int-test/<int:part_int_id>/", parts_by_int),
    path("parts-slug-test/<slug:part_slug>/", parts_by_slug),
]
