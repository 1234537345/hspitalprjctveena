# Generated by Django 4.2.16 on 2024-09-26 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0020_rename_departments_department_department_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='department',
            new_name='departments',
        ),
        migrations.RenameField(
            model_name='doctor',
            old_name='department',
            new_name='departments',
        ),
    ]
