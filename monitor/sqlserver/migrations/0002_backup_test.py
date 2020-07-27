# Generated by Django 2.1.5 on 2019-01-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlserver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='backup_test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('database_name', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField()),
                ('finish_date', models.DateTimeField()),
                ('backup_type', models.CharField(max_length=30)),
                ('backup_size_mb', models.FloatField()),
                ('compress_size_mb', models.FloatField()),
                ('physical_device_name', models.CharField(max_length=600)),
                ('user_name', models.CharField(max_length=100)),
            ],
        ),
    ]
