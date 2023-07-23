from django.db import models
from django.contrib.auth.models import User


class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apartment_number = models.CharField(max_length=10)

    # Add more fields as per your requirements

    def __str__(self):
        return self.user.username


class MaintenanceRequest(models.Model):
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    # Add more fields as per your requirements

    def __str__(self):
        return self.description


class ServiceVendor(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)

    # Add more fields as per your requirements

    def __str__(self):
        return self.name


class MaintenanceTask(models.Model):
    request = models.ForeignKey(MaintenanceRequest, on_delete=models.CASCADE)
    vendor = models.ForeignKey(ServiceVendor, on_delete=models.CASCADE)
    date_assigned = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    # Add more fields as per your requirements

    def __str__(self):
        return f"{self.request} - {self.vendor}"
