from django.contrib import admin
from . models import Project

class ProjectAdmin(admin.ModelAdmin):
    fields = ['project_name', 'project_description', 'project_url']

admin.site.register(Project, ProjectAdmin)