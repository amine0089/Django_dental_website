# Generated by Django 3.0.8 on 2020-07-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('stage', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
            ],
        ),
    ]