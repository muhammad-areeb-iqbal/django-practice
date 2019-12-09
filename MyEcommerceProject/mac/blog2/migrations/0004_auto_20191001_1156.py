# Generated by Django 2.2.4 on 2019-10-01 06:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0003_auto_20190927_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='post2model',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post2model',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
