from django.db import models
from authentication.models import Owner
# Create your models here.


class GovermentCorp(models.Model):
    corp_name = models.CharField(max_length=250)
    energy_rate = models.SmallIntegerField()
    selling_cost = models.SmallIntegerField()

    def __str__(self):
        return self.corp_name


class RenewableEnergy(models.Model):
    ENERGY_TYPE = (
        ('Solar', 'Solar'),
        ('Wind', 'Wind'),
        ('GeoThermal', 'Geothermal'),
    )

    type = models.CharField(max_length=60, choices=ENERGY_TYPE)
    installed_date = models.DateField(auto_now_add=True)
    potential_capacity = models.IntegerField()


class House(models.Model):

    owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE, related_name='owner')
    address = models.CharField(max_length=250)
    govt_corp = models.ForeignKey(GovermentCorp, on_delete=models.CASCADE)
    no_inhabitants = models.SmallIntegerField()
    joined = models.DateField(auto_now_add=True)
    energy_created_today = models.SmallIntegerField()

    def __str__(self):
        return self.owner+" House"

    def energy_today(self):
        total = 0
        total += self.energy_created_today
        return total
