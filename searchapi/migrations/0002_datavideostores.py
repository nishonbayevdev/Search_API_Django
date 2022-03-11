# Generated by Django 4.0.2 on 2022-03-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataVideoStores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
                ('video', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Malumotlar',
            },
        ),
    ]
