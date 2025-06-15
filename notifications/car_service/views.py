from django.http import HttpResponse, HttpRequest


def car_service_home_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Car service home page content")


def parts(request: HttpRequest, part_id: int) -> HttpResponse:
    return HttpResponse(f"<h1>Запчасти</h1><p>Запчасть #{part_id}</p>")
