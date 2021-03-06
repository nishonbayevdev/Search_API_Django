# Generated by Django 4.0.2 on 2022-02-21 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataImageStores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='media/Images')),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Malumotlar',
            },
        ),
    ]
