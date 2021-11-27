from django.db import models
from authentication.models import Owner
# Create your models here.


class GovernmentCorp(models.Model):
    corp_name = models.CharField(max_length=250)
    energy_rate = models.SmallIntegerField()
    selling_cost = models.SmallIntegerField()
    address = models.CharField(blank=True, max_length=250)

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
    effeciency_rate = models.SmallIntegerField(default=70)

    def __str__(self):
        return self.type


ROOM_TYPE = (
    ('Kitchen', 'Kitchen'),
    ('Bedroom', 'Bedroom'),
    ('Common_Area', 'Common_Area'),
)


class Room(models.Model):
    name = models.CharField(max_length=150, default=ROOM_TYPE[1][0])
    room_type = models.CharField(max_length=100, choices=ROOM_TYPE)
    energy_use = models.IntegerField()
    no_of_appliances = models.SmallIntegerField()

    def __str__(self) -> str:
        return self.name


class House(models.Model):

    owner = models.ForeignKey(
        Owner, on_delete=models.CASCADE, related_name='owner')
    address = models.CharField(max_length=250)
    rooms = models.ManyToManyField(Room)
    govt_corp = models.ForeignKey(GovernmentCorp, on_delete=models.CASCADE)
    renewable_energy = models.ForeignKey(
        RenewableEnergy, on_delete=models.CASCADE)
    no_inhabitants = models.SmallIntegerField()
    joined = models.DateField(auto_now_add=True)
    energy_created_today = models.SmallIntegerField()
    total_energy = models.IntegerField(default=1000)

    def __str__(self):
        return self.owner.username + " House"

    def energy_today(self):
        total = 0
        total += self.energy_created_today
        return total
