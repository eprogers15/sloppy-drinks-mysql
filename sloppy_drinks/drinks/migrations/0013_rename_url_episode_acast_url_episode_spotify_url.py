# Generated by Django 4.2.10 on 2024-02-26 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0012_remove_image_id_alter_image_filename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='url',
            new_name='acast_url',
        ),
        migrations.AddField(
            model_name='episode',
            name='spotify_url',
            field=models.URLField(default='https://open.spotify.com/show/3qFjDCQ16YrjFw5ufNpV3c?si=4202cac534494845'),
        ),
    ]
