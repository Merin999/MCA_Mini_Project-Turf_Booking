# Generated by Django 3.2 on 2021-12-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turf', '0021_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownerreg',
            name='owner_licence',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
