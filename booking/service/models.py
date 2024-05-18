from django.db import models

class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
        ('expired', 'Expired'),
        ('failed', 'Failed'),
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),

    )

    user_id = models.IntegerField()  # Assuming user identification via user ID
    garage_id = models.IntegerField()  # ID of the garage
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Booking {self.id} for User {self.user_id}"
