from django.db import models

# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()


class Referral(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    referral_date = models.DateField()
    referrer_name = models.CharField(max_length=255)
    referral_reason = models.TextField(max_length=255)
    note = models.TextField()
    document = models.FileField(
        upload_to='referral_documents/', null=True, blank=True)
