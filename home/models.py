from django.db import models

class Tags(models.Model):
    pass

class Project(models.Model):
    project_name = models.CharField(max_length=30)
    project_description = models.TextField(max_length=300, blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    project_img = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.project_name