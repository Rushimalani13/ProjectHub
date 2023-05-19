from django.apps import apps
from django.contrib import admin
from projects.models import uploadProject

# Register your models here.
for model in apps.get_app_config('projects').get_models():
    admin.site.register(model)
  