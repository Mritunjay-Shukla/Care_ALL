# Generated by Django 2.2.5 on 2020-07-19 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Care', '0003_auto_20200719_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gig',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccount.Profile'),
        ),
    ]
