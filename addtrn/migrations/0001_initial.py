# Generated by Django 4.1.1 on 2022-10-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trname', models.CharField(max_length=100)),
                ('fromstn', models.CharField(max_length=100)),
                ('tostn', models.CharField(max_length=100)),
                ('Deptime', models.CharField(max_length=25)),
                ('arrtime', models.CharField(max_length=25)),
            ],
        ),
    ]