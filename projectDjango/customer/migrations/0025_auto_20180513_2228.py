# Generated by Django 2.0.3 on 2018-05-13 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0024_auto_20180513_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='money',
            old_name='img_slip',
            new_name='image_slip',
        ),
        migrations.AlterField(
            model_name='money',
            name='resever_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.Reserve'),
        ),
    ]
