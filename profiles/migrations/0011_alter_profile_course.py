# Generated by Django 4.0.4 on 2022-05-22 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='course',
            field=models.CharField(choices=[('0', 'B.Tech'), ('1', 'MCA'), ('2', 'M.Tech'), ('3', 'MBA')], default=0, max_length=10),
        ),
    ]
