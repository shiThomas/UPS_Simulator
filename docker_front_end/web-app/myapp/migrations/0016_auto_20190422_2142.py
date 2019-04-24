# Generated by Django 2.2 on 2019-04-23 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20190422_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='truck_status',
            field=models.SmallIntegerField(choices=[(1, 'idle'), (2, 'traveling'), (3, 'arrive warehouse'), (4, 'loading'), (5, 'loaded'), (6, 'delivering')], default=1),
        ),
    ]