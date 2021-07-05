from django.shortcuts import render
from .models import Project


def home(request):
    datas = Project.objects.all()
    return render(request, 'frontend/portfolio/home.html', {'projects': datas})
