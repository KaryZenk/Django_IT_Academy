# Generated by Django 3.1.2 on 2020-10-27 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='genre',
            new_name='genres',
        ),
    ]
