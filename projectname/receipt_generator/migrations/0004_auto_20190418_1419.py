# Generated by Django 2.0.2 on 2019-04-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_generator', '0003_auto_20190418_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='address',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='donor',
            name='address',
            field=models.CharField(max_length=500),
        ),
    ]
