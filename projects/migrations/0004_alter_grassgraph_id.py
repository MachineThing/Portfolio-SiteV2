# Generated by Django 3.2.3 on 2021-05-14 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20210213_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grassgraph',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
