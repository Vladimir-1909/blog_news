# Generated by Django 3.1.4 on 2020-12-25 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201225_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='user',
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='Mail',
        ),
    ]
