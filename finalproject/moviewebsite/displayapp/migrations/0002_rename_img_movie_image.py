# Generated by Django 5.0.2 on 2024-02-19 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('displayapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='img',
            new_name='image',
        ),
    ]