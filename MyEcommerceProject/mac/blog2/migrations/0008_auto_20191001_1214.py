# Generated by Django 2.2.4 on 2019-10-01 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0007_auto_20191001_1210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post2model',
            name='title',
            field=models.CharField(error_messages={'blank': 'This field is not full pelase. give some title.', 'null': 'This field is not full pelase. give some title.', 'unique': 'This title is not unique, please try again.'}, help_text='Must be a unique Title.', max_length=240, unique=True, verbose_name='Post Title'),
        ),
    ]
