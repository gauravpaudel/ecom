# Generated by Django 3.1.5 on 2021-01-20 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210113_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]