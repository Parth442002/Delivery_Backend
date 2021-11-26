# Generated by Django 3.2.9 on 2021-11-26 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GovermentCorp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corp_name', models.CharField(max_length=250)),
                ('energy_rate', models.SmallIntegerField()),
                ('selling_cost', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RenewableEnergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Solar', 'Solar'), ('Wind', 'Wind'), ('GeoThermal', 'Geothermal')], max_length=60)),
                ('installed_date', models.DateField(auto_now_add=True)),
                ('potential_capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('no_inhabitants', models.SmallIntegerField()),
                ('joined', models.DateField(auto_now_add=True)),
                ('energy_created_today', models.SmallIntegerField()),
                ('govt_corp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.govermentcorp')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]