# Generated by Django 5.1.1 on 2024-10-09 09:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0040_alter_product_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Store.productcategory'),
        ),
    ]
