# Generated by Django 5.0 on 2024-12-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_prestador_mat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controle',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Imagem 1'),
        ),
    ]
