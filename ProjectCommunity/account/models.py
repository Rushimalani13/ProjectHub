from django.db import models

# Create your models here.
class profile(models.Model):
    sid = models.AutoField(primary_key=True)
    username=models.CharField(max_length=80)
    fname=models.CharField(max_length=220)
    lname=models.CharField(max_length=220)
    email=models.CharField(max_length=220)
    phone=models.CharField(max_length=20)
    College=models.TextField()
    course=models.TextField()
    passyear=models.CharField(max_length=10)
    profilePic=models.FileField(upload_to='media-root/profiles')

    
class teacherProfile(models.Model):
    tid = models.AutoField(primary_key=True)
    username=models.CharField(max_length=80)
    fname=models.CharField(max_length=220)
    lname=models.CharField(max_length=220)
    email=models.CharField(max_length=220)
    phone=models.CharField(max_length=20)
    College=models.TextField()
    course=models.TextField()
    idproof=models.FileField(upload_to='media-root/idproof')
    profilePic=models.FileField(upload_to='media-root/teacherprofiles')
 