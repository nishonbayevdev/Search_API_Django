# Generated by Django 4.0.2 on 2022-03-13 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapi', '0003_toursdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toursdata',
            name='price',
            field=models.FloatField(),
        ),
    ]
