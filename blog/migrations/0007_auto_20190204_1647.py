# Generated by Django 2.1.5 on 2019-02-04 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190204_1644'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='date',
            new_name='created',
        ),
    ]
