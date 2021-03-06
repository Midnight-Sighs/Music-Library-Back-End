# Generated by Django 3.2.7 on 2021-10-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_like_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(default='none', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='like_counter',
            field=models.IntegerField(),
        ),
    ]
