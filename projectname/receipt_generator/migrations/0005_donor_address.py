# Generated by Django 2.0.2 on 2019-04-10 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_generator', '0004_auto_20190409_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='address',
            field=models.TextField(default=''),
        ),
    ]