# Generated by Django 4.2.5 on 2023-10-08 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0014_coupon'),
        ('order', '0002_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='variant',
            field=models.ForeignKey(default=31, on_delete=django.db.models.deletion.CASCADE, to='product.productvariant'),
            preserve_default=False,
        ),
    ]
