# Generated by Django 4.1.13 on 2024-05-09 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfol', '0016_port_github'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='github',
            field=models.CharField(default=0.0004940711462450593, max_length=70),
            preserve_default=False,
        ),
    ]
