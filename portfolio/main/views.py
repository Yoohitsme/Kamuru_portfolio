from django.shortcuts import get_object_or_404, render
from portfolio.main.models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'home.html', {'projects': projects})

def about(request):
    return render(request, 'about.html')

def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    return render(request, 'project_detail.html', {'project': project})

from django.shortcuts import render, redirect
from .models import contacts

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contacts.objects.create(
            name=name,
            email=email,
            message=message
        )
        return redirect('/')  # after submit

    return render(request, 'contacts.html')