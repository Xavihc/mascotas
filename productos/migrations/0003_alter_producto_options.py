# Generated by Django 3.2.3 on 2021-07-06 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'permissions': (('gerente', 'Es gerente'), ('cliente', 'Es cliente'))},
        ),
    ]
