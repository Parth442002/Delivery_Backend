# Generated by Django 3.2.9 on 2021-11-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='total_energy',
            field=models.IntegerField(default=1000),
        ),
    ]
