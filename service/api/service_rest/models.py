from django.db import models
from django.urls import reverse

# Create your models here.

class AutomobileVO(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    import_href = models.CharField(max_length=200, unique=True)


class Technician(models.Model):
    name = models.CharField(max_length=50)
    employee_number = models.IntegerField(unique=True)


class Appointment(models.Model):
    vin = models.CharField(max_length=17)
    owner = models.CharField(max_length=100)
    date_and_time = models.DateTimeField()
    technician = models.ForeignKey(
        Technician,
        related_name="appointments",
        on_delete=models.PROTECT,
    )
    reason = models.TextField(max_length=400)
    vip = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)

    def get_api_url(self):
        return reverse('show_appointment', kwargs={"pk": self.id})
