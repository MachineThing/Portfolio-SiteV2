# Generated by Django 3.2.6 on 2021-08-31 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_staticpage_hiddel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='navbar',
            name='identifier',
        ),
    ]
