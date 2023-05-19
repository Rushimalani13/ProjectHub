from django.db import models
import datetime
from account.models import profile
# Create your models here.
class ProjectEvents(models.Model):
    peid = models.AutoField(primary_key=True)
    title=models.CharField(max_length=220)
    description=models.TextField()
    fronposter=models.FileField(upload_to='media-root/ProjectPoster')
    eventdate=models.DateField(("Date"), default=datetime.date.today)
    eventtime=models.DateTimeField(auto_now_add=True, blank=True)
    
class ProjectEventEntry(models.Model):
    peeid=models.AutoField(primary_key=True)
    peinfo =models.ForeignKey(ProjectEvents, on_delete=models.CASCADE)
    userinfo=models.ForeignKey(profile, on_delete=models.CASCADE)
    