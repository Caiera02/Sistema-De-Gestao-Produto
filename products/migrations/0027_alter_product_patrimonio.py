# Generated by Django 5.0 on 2024-12-13 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='patrimonio',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.prestador', verbose_name='Prestador'),
        ),
    ]
