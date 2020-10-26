# Generated by Django 3.1.2 on 2020-10-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Автор книги')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Автор книги из справочника')),
            ],
        ),
        migrations.CreateModel(
            name='BookGenre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Жанр книги')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание жанра')),
            ],
        ),
        migrations.CreateModel(
            name='BookSeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Серия книг')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание серии книг')),
            ],
        ),
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Издательство')),
            ],
        ),
    ]
