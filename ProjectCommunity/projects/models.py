from django.db import models

# Create your models here.
class uploadProject(models.Model):
    pid = models.AutoField(primary_key=True)
    username=models.CharField(max_length=80)
    fname=models.CharField(max_length=220)
    lname=models.CharField(max_length=220)
    email=models.CharField(max_length=220)
    College=models.TextField()
    course=models.TextField()
    projectname=models.CharField(max_length=220)
    tags=models.TextField()
    description=models.TextField()
    zip_project=models.FileField(upload_to='media-root/zip_projects')
    outputSS=models.FileField(upload_to='media-root/outputSS')

class collegeList(models.Model):
    cid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=80)
    location=models.CharField(max_length=220)
    description=models.TextField()
    outputSS=models.FileField(upload_to='media-root/college_img')


class Courses(models.Model):
    crid = models.AutoField(primary_key=True)
    name=models.CharField(max_length=80)

class TreandingProjects(models.Model):
    tpid = models.AutoField(primary_key=True)
    title=models.CharField(max_length=220)
    description=models.TextField()
    frontimg=models.FileField(upload_to='media-root/treandingProject')