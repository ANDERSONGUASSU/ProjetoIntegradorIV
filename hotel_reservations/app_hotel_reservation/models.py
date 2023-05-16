from django.db import models


class Simulador_Reservas(models.Model):
    Booking_ID = models.AutoField(primary_key=True)
    no_of_adults = models.IntegerField()
    no_of_children = models.IntegerField()
    no_of_weekend_nights = models.IntegerField()
    no_of_week_nights = models.IntegerField()
    type_of_meal_plan = models.TextField()
    required_car_parking_space = models.IntegerField()
    room_type_reserved = models.TextField()
    lead_time = models.IntegerField()
    arrival_year = models.IntegerField()
    arrival_month = models.IntegerField()
    arrival_date = models.IntegerField()
    market_segment_type = models.TextField()
    repeated_guest = models.IntegerField()
    no_of_previous_cancellations = models.IntegerField()
    no_of_previous_bookings_not_canceled = models.IntegerField()
    avg_price_per_room = models.FloatField()
    no_of_special_requests = models.IntegerField()
