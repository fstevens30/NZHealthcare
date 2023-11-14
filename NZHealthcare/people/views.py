from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person, Referral

# Create your views here.

# Home page view


def home(request):
    return render(request, 'home.html')


@login_required
def people_list(request):
    people = Person.objects.all()
    return render(request, 'people_list.html', {'people': people})


@login_required
def referrals_list(request):
    referrals = Referral.objects.all()
    return render(request, 'referrals_list.html', {'referrals': referrals})


@login_required
def person_detail(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    referrals = Referral.objects.filter(person=person)
    return render(request, 'person_detail.html', {'person': person, 'referrals': referrals})


@login_required
def referral_detail(request, referral_id):
    referral = get_object_or_404(Referral, id=referral_id)
    return render(request, 'referral_detail.html', {'referral': referral})
