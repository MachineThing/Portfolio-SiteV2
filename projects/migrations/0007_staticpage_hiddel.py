# Generated by Django 3.2.6 on 2021-08-31 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_staticpage_navbar'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticpage',
            name='hiddel',
            field=models.BooleanField(default=False),
        ),
    ]
