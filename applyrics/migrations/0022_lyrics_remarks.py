# Generated by Django 2.0.3 on 2018-04-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applyrics', '0021_lyrics_replaced_new_lines'),
    ]

    operations = [
        migrations.AddField(
            model_name='lyrics',
            name='remarks',
            field=models.TextField(default='You can submit a correction if something is wrong with the lyrics.', max_length=100),
            preserve_default=False,
        ),
    ]