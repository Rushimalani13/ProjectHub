from django.apps import apps
from django.contrib import admin
from account.models import profile
from account.models import teacherProfile
# Register your models here.
for model in apps.get_app_config('account').get_models():
    admin.site.register(model)
  