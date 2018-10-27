# Generated by Django 2.1.1 on 2018-10-27 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mindmaps', '0003_map_mapjson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='friendly_url',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='map',
            name='language',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='map',
            name='mapjson',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='map',
            name='public_id',
            field=models.CharField(max_length=16, null=True),
        ),
    ]