# Generated by Django 3.2 on 2021-05-07 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turf', '0016_auto_20210430_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookturf',
            name='pack',
            field=models.CharField(max_length=50, null=True),
        ),
    ]