# Generated by Django 5.0.7 on 2024-08-07 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0004_alter_dog_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='age',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='dog',
            name='name',
        ),
    ]
