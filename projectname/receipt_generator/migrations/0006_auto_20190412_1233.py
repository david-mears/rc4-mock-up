# Generated by Django 2.0.2 on 2019-04-12 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receipt_generator', '0005_donor_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='charity',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='receipt_generator.Charity'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=14, verbose_name='The amount received'),
        ),
    ]