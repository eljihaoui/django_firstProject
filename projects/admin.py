from django.contrib import admin

# Register your models here.
from . models import Projet
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('titre','description')
admin.site.register(Projet,ProjectAdmin)