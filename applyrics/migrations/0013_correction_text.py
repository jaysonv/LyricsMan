# Generated by Django 2.0.3 on 2018-03-30 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyrics', '0012_correction_song_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='correction',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
