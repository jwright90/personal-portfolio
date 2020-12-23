from django.contrib import admin
from . models import Project

class ProjectAdmin(admin.ModelAdmin):
    fields = ['project_name', 'project_description', 'project_url', 'project_img']

admin.site.register(Project, ProjectAdmin)