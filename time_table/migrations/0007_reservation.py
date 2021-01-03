# Generated by Django 3.1.3 on 2021-01-03 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_table', '0006_merge_20201226_0308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(default='건물이름', max_length=10)),
                ('floor', models.CharField(max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day_of_the_week', models.CharField(max_length=1)),
                ('description', models.TextField()),
            ],
        ),
    ]
