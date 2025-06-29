from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def homepage_view(request: HttpRequest) -> HttpResponse:
    context = {
        "header": "Peugeot Car Service",
    }

    return render(
        request=request,
        template_name="car_service/homepage.html",
        context={"homepage": context},
    )
