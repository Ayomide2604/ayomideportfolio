from multiprocessing import context
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import *
def index(request):
    skills = Skills.objects.all()
    facts = Facts.objects.all()
    projects = Project.objects.all()
    context = {'skills': skills, 'facts': facts, 'projects': projects}
    return render(request, 'pages/index.html', context)


def project(request, pk):
    project = get_object_or_404(Project, id=pk)
    context = {'project': project}
    return render(request, 'pages/portfolio-details.html', context)