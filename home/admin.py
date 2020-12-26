from django.contrib import admin
from . models import Project, Tag

class ProjectAdmin(admin.ModelAdmin):
    fields = ['project_name', 'project_description', 'project_url', 'project_img_static', 'project_img_gif', 'tags']

admin.site.register(Project, ProjectAdmin)

class TagAdmin(admin.ModelAdmin):
    fields = ['tag_name']

admin.site.register(Tag, TagAdmin)