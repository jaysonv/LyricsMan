# Generated by Django 2.0.3 on 2018-03-30 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyrics', '0007_auto_20180330_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lyrics',
            name='text',
            field=models.TextField(),
        ),
    ]
