# Generated by Django 5.0.2 on 2024-03-06 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_doctor_job_end_remove_doctor_job_start_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='book_time',
            field=models.CharField(choices=[('08:00 - 09:30', '08:00 - 09:30'), ('09:30 - 11:00', '09:30 - 11:00'), ('11:00 - 12:00', '11:00 - 12:00'), ('13:00 - 14:30', '13:00 - 14:30'), ('14:30 - 16:30', '14:30 - 16:30')], max_length=255),
        ),
    ]
