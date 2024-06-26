"""
URL configuration for NZHealthcare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from patients import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('patients/', views.patient_list, name='patient_list'),
    path('referrals/', views.referrals_list, name='referrals_list'),
    path('patient/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('referral/<int:referral_id>/',
         views.referral_detail, name='referral_detail'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_referral/<int:patient_id>/',
         views.add_referral, name='add_referral'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('referral/<int:referral_id>/view_document/',
         views.view_document, name='view_document'),
]
