from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Patient, Referral

# Create your views here.


def home(request):
    return render(request, 'home.html')


@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})


@login_required
def referrals_list(request):
    referrals = Referral.objects.all()
    return render(request, 'referrals_list.html', {'referrals': referrals})


@login_required
def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    referrals = Referral.objects.filter(patient=patient)
    return render(request, 'patient_detail.html', {'patient': patient, 'referrals': referrals})


@login_required
def referral_detail(request, referral_id):
    referral = get_object_or_404(Referral, id=referral_id)
    return render(request, 'referral_detail.html', {'referral': referral})
