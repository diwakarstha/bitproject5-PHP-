# Generated by Django 3.1.4 on 2021-01-07 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0017_auto_20210106_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=1000000),
        ),
    ]
