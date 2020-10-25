# Generated by Django 3.1.2 on 2020-10-25 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_author', models.CharField(max_length=50, verbose_name='Авторы книги')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Авторы книги из справочника')),
            ],
        ),
    ]