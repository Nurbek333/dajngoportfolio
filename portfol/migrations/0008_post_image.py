# Generated by Django 4.1.13 on 2024-05-07 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfol', '0007_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images/'),
        ),
    ]
