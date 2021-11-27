from django.contrib import admin
from .models import House, GovernmentCorp, RenewableEnergy, Room
# Register your models here.

admin.site.register(House)
admin.site.register(GovernmentCorp)
admin.site.register(RenewableEnergy)
admin.site.register(Room)
