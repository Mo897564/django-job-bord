from django.contrib import admin

# Register your models here.

from . models import *


admin.site.register(job)
admin.site.register(Categry)
admin.site.register(Apply)

