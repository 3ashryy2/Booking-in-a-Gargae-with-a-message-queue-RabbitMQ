from django.db import models

class BookingRequest(models.Model):
    booking_id = models.IntegerField()
    garage_id = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, default='pending')  # 'pending', 'confirmed', 'rejected'

    def __str__(self):
        return f"Booking {self.booking_id} status {self.status}"
