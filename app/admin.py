from django.contrib import admin
from .models import Projects, Employee, ProjectDiscription, Skills


# Register your models here.

admin.site.register(Projects)
admin.site.register(Employee)
admin.site.register(ProjectDiscription)
admin.site.register(Skills)
