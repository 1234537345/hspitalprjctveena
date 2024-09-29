# Generated by Django 4.2.16 on 2024-09-28 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0024_prescription'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('expiry_date', models.DateField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
