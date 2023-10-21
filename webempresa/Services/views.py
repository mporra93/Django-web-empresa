from django.shortcuts import render

from .models import Service

# Create your views here.


def services(request):
    services = Service.objects.all()
    return render(request, "Services/services.html", {'services':services} )