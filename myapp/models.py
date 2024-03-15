from django.contrib.auth.models import User
from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    job = models.CharField(max_length=255)

    def __str__(self):
        return f'({self.name} {self.surname} {self.job})'

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'


class Booking(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_time = models.CharField(max_length=255,default='---------',choices=[
        ('08:00 - 09:30','08:00 - 09:30'),
        ('09:30 - 11:00','09:30 - 11:00'),
        ('11:00 - 12:00','11:00 - 12:00'),
        ('13:00 - 14:30','13:00 - 14:30'),
        ('14:30 - 16:30','14:30 - 16:30'),

    ])

    def __str__(self):
        return f'Customer: ({str(self.user)}) to Doctor: ({str(self.doctor)}) at ({self.book_time}) '

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

class Times(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
