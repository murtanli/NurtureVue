# Generated by Django 4.1.3 on 2023-06-22 18:29

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
            name='greenhouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imei', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=90)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=90)),
            ],
        ),
        migrations.CreateModel(
            name='reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('description', models.TextField(blank=True)),
                ('rate_plants', models.CharField(max_length=10)),
                ('harvest', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='registry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('humidity', models.IntegerField()),
                ('water', models.IntegerField()),
                ('temperature', models.IntegerField()),
                ('energy', models.IntegerField()),
                ('soil_moisture', models.IntegerField()),
                ('brightness_of_lights', models.IntegerField()),
                ('heating', models.IntegerField()),
                ('ventilation', models.IntegerField()),
                ('window1', models.IntegerField()),
                ('window2', models.IntegerField()),
                ('pump1', models.IntegerField()),
                ('pump2', models.IntegerField()),
                ('error', models.IntegerField()),
                ('greenhouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.greenhouse')),
                ('report', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.reports')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('number_phone', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='greenhouse',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.profile'),
        ),
    ]
