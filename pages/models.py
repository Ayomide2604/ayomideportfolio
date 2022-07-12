from datetime import date
from django.db import models
from django.urls import reverse

# Create your models here.

class Facts(models.Model):
    happy_clients = models.IntegerField()
    number_of_projects = models.IntegerField()
    hours_of_support = models.IntegerField()
    certifications = models.IntegerField()
    freelance = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'facts'

    def __str__(self):
        return str(self.happy_clients)

class Skills(models.Model):
    name = models.CharField(max_length=255)
    level = models.IntegerField()

    class Meta:
        verbose_name_plural = 'skills'

    def __str__(self):
        return self.name



class ProjectCategory(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True, null=True)

    class Meta:
        verbose_name_plural = 'Project Categories'

    def __str__(self):
        return self.name

class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True)    
    name = models.CharField(max_length=255)
    client = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    photo_main = models.ImageField(upload_to= 'project/%Y/%m/%d' ,blank=True, null=True)
    photo_1 = models.ImageField(upload_to= 'project/%Y/%m/%d', blank=True, null=True)
    photo_2 = models.ImageField(upload_to= 'project/%Y/%m/%d', blank=True, null=True)

    def get_absolute_url(self):
        return reverse("project-detail", args=[self.id])
    

    def __str__(self):
        return self.name


