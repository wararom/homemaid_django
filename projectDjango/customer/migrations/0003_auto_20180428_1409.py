# Generated by Django 2.0.3 on 2018-04-28 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20180427_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(null=True, upload_to='piccustomer'),
        ),
        migrations.AddField(
            model_name='maid',
            name='image',
            field=models.ImageField(null=True, upload_to='picmaid'),
        ),
    ]
