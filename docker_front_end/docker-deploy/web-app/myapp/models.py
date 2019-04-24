from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

PACKAGE_STATUS = (
    (0, 'Preparing for delivery'),
    (1, 'In transit'),
    (2, 'Delivered')
)

Truck_STATUS = (
    (1, 'idle'),
    (2, 'traveling'),
    (3, 'arrive warehouse'),
    (4, 'loading'),
    (5, 'loaded'),
    (6, 'delivering')
)


class truck(models.Model):
    truck_id = models.IntegerField()
    truck_status = models.SmallIntegerField(choices=Truck_STATUS, default=1)

    def __str__(self):
        return f'{self.truck_id},{self.truck_status}'


class package(models.Model):
    package_id = models.BigIntegerField()
    owner =models.CharField(max_length=50,blank=True,null=True)
    truckid = models.IntegerField(null=True)
    destination_x = models.IntegerField(null=True)
    destination_y = models.IntegerField(null=True)
    package_status = models.SmallIntegerField(choices=PACKAGE_STATUS, default=0)
    description = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return f'{self.package_id},{self.destination_x},{self.destination_y}'

    def get_absolute_url(self):
        return reverse('package-detail', args=[str(self.id)])




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Phone_number = models.CharField(max_length=30, verbose_name="Phone Number", blank=True)

    Address = models.CharField(
        max_length=50,
        verbose_name="Address",
        blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class survey(models.Model):
    package_id = models.BigIntegerField()
    satisfied = models.CharField(max_length=1,blank=True,null=True)
    content = models.CharField(max_length=300,blank = True,null=True)

    def __str__(self):
        return f'{self.package_id},{self.satisfied}'

    def get_absolute_url(self):
        return reverse('index')