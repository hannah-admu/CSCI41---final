# Generated by Django 5.0.2 on 2024-12-02 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalItem',
            fields=[
                ('item_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='CrewPersonnel',
            fields=[
                ('employee_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_initial', models.CharField(blank=True, max_length=5)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('city_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('city_name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('airport', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('origin', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('passenger_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Plane',
            fields=[
                ('plane_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('schedule_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FlightCrew',
            fields=[
                ('crew_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_scheduler.crewpersonnel')),
            ],
        ),
        migrations.CreateModel(
            name='ItemBilling',
            fields=[
                ('billing_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('additional_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_scheduler.additionalitem')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('booking_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_scheduler.flight')),
                ('item_billing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_scheduler.itembilling')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_scheduler.passenger')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('route_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('departed_city', models.CharField(max_length=100)),
                ('departure_time', models.TimeField()),
                ('arrival_time', models.TimeField()),
                ('expected_travel_time', models.DurationField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_scheduler.destination')),
            ],
        ),
        migrations.AddField(
            model_name='flight',
            name='schedule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flight_scheduler.schedule'),
        ),
    ]
