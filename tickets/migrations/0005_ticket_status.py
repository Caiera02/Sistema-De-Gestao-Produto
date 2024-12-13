# Generated by Django 5.0 on 2024-12-13 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_alter_status_options_alter_ticket_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='filial', to='tickets.status', verbose_name='Status'),
            preserve_default=False,
        ),
    ]