# Generated by Django 3.0 on 2021-08-17 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvs', '0002_auto_20210813_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='csv',
            name='images_file',
            field=models.FileField(blank=True, upload_to='csvs'),
        ),
    ]
