from django.http import HttpResponse, HttpRequest


def car_service_home_page(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Car service home page content")


def parts_by_int(request: HttpRequest, part_int_id: int) -> HttpResponse:
    return HttpResponse(f"<h1>Запчасти</h1><p>Запчасть #{part_int_id}</p>")


def parts_by_slug(request: HttpRequest, part_slug: str) -> HttpResponse:
    return HttpResponse(f"<h1>Запчасти</h1><p>Запчасть #{part_slug}</p>")
