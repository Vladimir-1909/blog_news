# Generated by Django 3.1.4 on 2020-12-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201225_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[(' ', ' '), ('m', 'Man'), ('w', 'Woman')], default='', max_length=1),
        ),
    ]
