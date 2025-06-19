from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def car_service_homepage(request: HttpRequest) -> HttpResponse:
    return render(
        request=request,
        template_name="car_service/car_service.html"
    )
