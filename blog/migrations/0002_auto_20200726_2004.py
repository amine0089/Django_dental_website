# Generated by Django 3.0.8 on 2020-07-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]