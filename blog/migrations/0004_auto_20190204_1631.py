# Generated by Django 2.1.5 on 2019-02-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190204_1626'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='blog',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
