# Generated by Django 3.0.6 on 2020-05-31 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('windletterapi', '0002_auto_20200531_0238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='divice_position',
            new_name='divice_position_lat',
        ),
        migrations.AddField(
            model_name='user',
            name='divice_position_lon',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
