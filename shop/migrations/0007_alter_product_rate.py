# Generated by Django 4.0.6 on 2022-07-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rate',
            field=models.FloatField(null=True),
        ),
    ]
