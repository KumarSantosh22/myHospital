# Generated by Django 2.0.1 on 2018-02-22 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_patient', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='case',
            name='receptionist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_receptionist', to=settings.AUTH_USER_MODEL),
        ),
    ]
