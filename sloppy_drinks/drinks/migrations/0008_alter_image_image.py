# Generated by Django 4.2.10 on 2024-02-16 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0007_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(max_length=200, unique=True, upload_to='images/'),
        ),
    ]
