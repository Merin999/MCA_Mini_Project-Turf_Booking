# Generated by Django 3.1.2 on 2021-04-11 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turf', '0006_remove_stadium_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='turf',
            name='image3',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
