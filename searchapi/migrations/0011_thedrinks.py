# Generated by Django 4.0 on 2022-04-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapi', '0010_phoneproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheDrinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Ichimlik nomi')),
                ('image', models.ImageField(upload_to='media/drinks', verbose_name='Ichimlik rasmi')),
                ('packageAt', models.DateField(auto_now=True)),
                ('endAt', models.DateField(verbose_name='Yaraqligigi')),
                ('description', models.TextField(verbose_name='Tarif')),
                ('isPublish', models.BooleanField(default=False, verbose_name='Korsatish')),
                ('volume', models.PositiveSmallIntegerField(verbose_name='hajmi L da')),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000, verbose_name='Narxi')),
                ('madePlace', models.PositiveSmallIntegerField(choices=[('UZ', 0), ('RU', 1), ('US', 2), ('EN', 3), ('FR', 4)], verbose_name='Ishlab chiqarilgan davlat')),
            ],
            options={
                'verbose_name_plural': 'Ichimliklar',
            },
        ),
    ]