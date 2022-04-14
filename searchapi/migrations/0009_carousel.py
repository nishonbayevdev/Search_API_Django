# Generated by Django 4.0.2 on 2022-03-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapi', '0008_devolopers_alter_foods_catagory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/carousel', verbose_name='Rasm')),
                ('name', models.CharField(max_length=128, verbose_name='Ism')),
                ('profesion', models.CharField(max_length=128, verbose_name='Kasb')),
                ('description', models.TextField(verbose_name='Tafsilot')),
                ('isShow', models.BooleanField(default=False, verbose_name="Ko'rsatish")),
            ],
            options={
                'verbose_name_plural': 'Carousel',
            },
        ),
    ]