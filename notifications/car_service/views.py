from django.http import HttpResponse, HttpRequest


def car_service_home_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Car service home page content")
