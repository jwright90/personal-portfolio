import json
from django.core import serializers
from django.shortcuts import render
from . models import Project, Tag


# Create your views here.
def home(request):

    projects = Project.objects.all()
    tags = Tag.objects.all()
    projects_json = serializers.serialize("json", projects)
    tags_json = serializers.serialize("json", tags)

    context = { 'projects' : projects, 
                'projects_json' : projects_json, 'tags_json' : tags_json}

    return render(request, 'home/home.html', context)

