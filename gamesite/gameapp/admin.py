from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here

# Grants the admin site access to Game
admin.site.register(Game)