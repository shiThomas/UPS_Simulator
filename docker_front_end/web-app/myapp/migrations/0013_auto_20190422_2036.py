# Generated by Django 2.2 on 2019-04-23 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20190422_2035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='package',
            old_name='Destination_X',
            new_name='destination_x',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='Destination_Y',
            new_name='destination_y',
        ),
    ]
