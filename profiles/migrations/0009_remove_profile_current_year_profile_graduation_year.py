# Generated by Django 4.0.4 on 2022-05-22 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_remove_profile_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='current_year',
        ),
        migrations.AddField(
            model_name='profile',
            name='graduation_year',
            field=models.DateField(null=True),
        ),
    ]
