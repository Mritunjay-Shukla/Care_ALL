# Generated by Django 2.2.5 on 2020-07-18 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fees',
            field=models.IntegerField(blank=True, default=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
