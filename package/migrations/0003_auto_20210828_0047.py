# Generated by Django 3.2.6 on 2021-08-28 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('package', '0002_auto_20210827_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='classify',
            name='is_delete',
            field=models.IntegerField(default=1, max_length=1),
        ),
        migrations.AddField(
            model_name='data',
            name='is_delete',
            field=models.IntegerField(default=1, max_length=1),
        ),
    ]
