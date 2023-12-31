# Generated by Django 4.2.6 on 2023-10-29 04:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('it', 'Italian'), ('iten', 'Japanese')], default='en', max_length=4),
        ),
    ]
