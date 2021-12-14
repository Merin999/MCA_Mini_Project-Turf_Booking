# Generated by Django 3.1.2 on 2021-04-24 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Turf', '0013_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pack', models.CharField(max_length=50)),
                ('turf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Turf.turf')),
            ],
        ),
        migrations.RemoveField(
            model_name='stadium',
            name='owner',
        ),
        migrations.DeleteModel(
            name='BookStadium',
        ),
        migrations.DeleteModel(
            name='Stadium',
        ),
    ]
