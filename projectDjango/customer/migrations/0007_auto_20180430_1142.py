# Generated by Django 2.0.3 on 2018-04-30 04:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20180430_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
