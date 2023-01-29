from django.shortcuts import render
from .models import Project, Header


def home(request):
    headers = Header.objects.all()
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects, 'headers': headers})

