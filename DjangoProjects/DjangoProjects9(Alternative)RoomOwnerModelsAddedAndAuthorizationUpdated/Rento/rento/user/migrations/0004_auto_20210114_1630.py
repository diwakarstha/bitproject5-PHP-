# Generated by Django 3.1.4 on 2021-01-14 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210114_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomowner',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=120, null=True),
        ),
    ]
