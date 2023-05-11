from django.contrib import admin

from .models import *


# Register your models here.


admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Medecin)
admin.site.register(Secretaire)
admin.site.register(Patient)
