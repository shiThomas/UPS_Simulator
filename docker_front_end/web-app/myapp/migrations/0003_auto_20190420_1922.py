# Generated by Django 2.2 on 2019-04-20 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190420_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Address',
            field=models.CharField(blank=True, max_length=50, verbose_name='Address'),
        ),
    ]
