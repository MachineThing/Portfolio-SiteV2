# Generated by Django 3.1.6 on 2021-02-13 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grassgraph',
            name='data',
            field=models.TextField(),
        ),
    ]
