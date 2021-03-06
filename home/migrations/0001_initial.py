# Generated by Django 3.0.8 on 2020-07-29 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('addresse', models.CharField(max_length=50)),
                ('scheldule', models.CharField(choices=[('9 AM to 10 AM', '9 AM to 10 AM'), ('11 AM to 12 AM', '11 AM to 12 AM'), ('2 PM to 4 PM', '2 PM to 4 PM'), ('8 PM to 10 PM', '8 PM to 10 PM')], max_length=50)),
            ],
            options={
                'verbose_name': 'apointment',
                'verbose_name_plural': 'apointments',
            },
        ),
    ]
