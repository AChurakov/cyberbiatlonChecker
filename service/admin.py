from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Team)
admin.site.register(Task)
admin.site.register(Def_service)
admin.site.register(Service)
admin.site.register(Complete_task)