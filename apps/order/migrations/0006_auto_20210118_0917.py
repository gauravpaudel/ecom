# Generated by Django 3.1.5 on 2021-01-18 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_auto_20210117_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paid_amount',
            new_name='amount_to_be_paid',
        ),
        migrations.AddField(
            model_name='order',
            name='cod',
            field=models.BooleanField(default=False),
        ),
    ]