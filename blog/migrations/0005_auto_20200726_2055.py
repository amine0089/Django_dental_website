# Generated by Django 3.0.8 on 2020-07-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'BlogPostss', 'verbose_name_plural': 'BlogPosts'},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True),
        ),
    ]