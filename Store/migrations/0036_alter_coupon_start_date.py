# Generated by Django 5.1.1 on 2024-10-05 09:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0035_alter_coupon_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 5, 9, 49, 19, 944122, tzinfo=datetime.timezone.utc)),
        ),
    ]
