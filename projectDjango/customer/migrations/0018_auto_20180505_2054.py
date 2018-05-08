# Generated by Django 2.0.3 on 2018-05-05 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_auto_20180502_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='customer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.Customer'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='postcode',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='customer',
            name='telephone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
