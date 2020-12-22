from django.db import models

class Tags(models.Model):
    pass

class Project(models.Model):
    project_name = models.CharField(max_length=30)
    project_description = models.TextField(max_length=300, blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    project_img = models.ImageField(blank=True, null=True)