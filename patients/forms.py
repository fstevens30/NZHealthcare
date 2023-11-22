from django import forms
from .models import Patient, Referral


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'phone_number', 'date_of_birth']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }


class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['referral_date', 'referrer_name',
                  'referral_reason', 'note', 'document']
        widgets = {
            'referral_date': forms.DateInput(attrs={'type': 'date'}),
        }
