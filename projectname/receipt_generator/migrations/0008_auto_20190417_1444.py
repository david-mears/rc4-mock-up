# Generated by Django 2.0.2 on 2019-04-17 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_generator', '0007_auto_20190412_1332'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receipt',
            old_name='receipt',
            new_name='receipt_pdf',
        ),
    ]