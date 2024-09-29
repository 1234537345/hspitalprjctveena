# Generated by Django 4.2.16 on 2024-09-24 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0016_patient_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp.patient'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='symptoms',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
