from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.SimpleUsers)
class SimpleUserAdmin(admin.ModelAdmin):
    pass
 