# Generated by Django 3.1.4 on 2021-01-06 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0015_auto_20210105_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image1',
            field=models.ImageField(default=1, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='image2',
            field=models.ImageField(default=2, upload_to='image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='room',
            name='image3',
            field=models.ImageField(default=5, upload_to='image'),
            preserve_default=False,
        ),
    ]
