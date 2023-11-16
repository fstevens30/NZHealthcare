from django.contrib import admin
from .models import Patient, Referral

# Register your models here.

admin.site.register(Patient)
admin.site.register(Referral)
