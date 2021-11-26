from django.contrib import admin
from .models import House, GovermentCorp, RenewableEnergy
# Register your models here.

admin.site.register(House)
admin.site.register(GovermentCorp)
admin.site.register(RenewableEnergy)
