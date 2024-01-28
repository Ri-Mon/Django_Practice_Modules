# Generated by Django 5.0.1 on 2024-01-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='father_name',
        ),
        migrations.AlterField(
            model_name='student',
            name='date_field',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_time_field',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='time_field',
            field=models.TimeField(auto_now_add=True),
        ),
    ]