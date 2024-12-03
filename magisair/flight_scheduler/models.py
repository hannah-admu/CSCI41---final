from django.db import models
from datetime import datetime 

# Create your models here.

class AdditionalItem(models.Model):
    item_no = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class ItemBilling(models.Model):
    billing_id = models.CharField(max_length=20, primary_key=True)
    additional_item = models.ForeignKey(AdditionalItem, on_delete=models.CASCADE)

class Passenger(models.Model):
    passenger_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10)

class Destination(models.Model):
    city_id = models.CharField(max_length=20, primary_key=True)
    city_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    airport = models.CharField(max_length=100)  

class Schedule(models.Model):
    schedule_id = models.CharField(max_length=20, primary_key=True)
    date = models.DateField()

class Flight(models.Model):
    flight_no = models.CharField(max_length=20, primary_key=True)
    origin = models.CharField(max_length=100)
    duration = models.DurationField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)

class Route(models.Model):
    route_id = models.CharField(max_length=20, primary_key=True)
    departed_city = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    expected_travel_time = models.DurationField()

    @property
    def actual_time(self):
        # calculate actual time (derived)
        arrival = datetime.combine(datetime.today(), self.arrival_time)
        departure = datetime.combine(datetime.today(), self.departure_time)
        return arrival - departure

class Booking(models.Model):
    booking_no = models.CharField(max_length=20, primary_key=True)
    flight_no = models.ForeignKey(Flight, on_delete=models.CASCADE)
    item_billing = models.ForeignKey(ItemBilling, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

class CrewPersonnel(models.Model):
    employee_id = models.CharField(max_length=20, primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(max_length=5, blank=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    role = models.CharField(max_length=50)

class FlightCrew(models.Model):
    crew_id = models.CharField(max_length=20, primary_key=True)
    employee = models.ForeignKey(CrewPersonnel, on_delete=models.CASCADE)

class Plane(models.Model):
    plane_no = models.CharField(max_length=20, primary_key=True)
    model = models.CharField(max_length=100)