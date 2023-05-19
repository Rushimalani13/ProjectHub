from django.contrib import admin
from django.apps import apps
from account.models import profile
from teacherdashboard.models import ProjectEvents,ProjectEventEntry

# Register your models here.
for model in apps.get_app_config('teacherdashboard').get_models():
    admin.site.register(model)