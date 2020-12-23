from django.shortcuts import render
from . models import Project
from PIL import Image

# Create your views here.
def home(request):

    projects = Project.objects.all()

    context = {'projects' : projects, }

    return render(request, 'home/home.html', context)

