from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Babysitter)
admin.site.register(Baby)
admin.site.register(Procure)
admin.site.register(Schoolfees)
admin.site.register(Dollsdashboard)