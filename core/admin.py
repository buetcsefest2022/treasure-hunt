from django.contrib import admin

# Register your models here.
from core.models import TeamProfile

models = [TeamProfile]
admin.site.register(models)
