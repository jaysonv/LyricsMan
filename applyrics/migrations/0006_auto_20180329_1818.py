# Generated by Django 2.0.3 on 2018-03-29 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applyrics', '0005_auto_20180329_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='lyrics',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
    ]