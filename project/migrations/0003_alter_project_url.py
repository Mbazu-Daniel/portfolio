# Generated by Django 4.0 on 2021-12-24 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_remove_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.URLField(max_length=1000),
        ),
    ]
