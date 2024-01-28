from django.shortcuts import render
from . import models

def home(request):
    student = models.Student.objects.all()
    return render(request, "home.html", {'data': student})
