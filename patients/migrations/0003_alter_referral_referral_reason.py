# Generated by Django 4.2.7 on 2023-11-21 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_alter_patient_first_name_alter_patient_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='referral_reason',
            field=models.TextField(max_length=80),
        ),
    ]