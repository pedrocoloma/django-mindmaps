# Generated by Django 2.1.1 on 2018-09-02 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mindmaps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mymaps', to='mindmaps.User'),
        ),
    ]
