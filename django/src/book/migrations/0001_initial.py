# Generated by Django 3.1.2 on 2020-10-26 23:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('handbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название Книги')),
                ('photo', models.ImageField(blank=True, height_field=100, null=True, upload_to='media/', verbose_name='Фото обложки', width_field=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Цена (BYN)')),
                ('year', models.IntegerField(validators=[django.core.validators.MaxValueValidator(3000), django.core.validators.MinValueValidator(0)], verbose_name='Год издания')),
                ('pages', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Кол-во страницы')),
                ('cover', models.CharField(choices=[('HC', 'Твёрдый переплёт'), ('SC', 'Мягкая обложка')], default='HC', max_length=2, verbose_name='Переплёт')),
                ('size', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(message='Формат: 120x80/32', regex='\\d{2,3}x\\d{2,3}/\\d{2,3}')], verbose_name='Формат')),
                ('isbn', models.CharField(blank=True, max_length=17, null=True, verbose_name='ISBN')),
                ('weight', models.IntegerField(blank=True, null=True, verbose_name='Вес (гр.)')),
                ('restrictions', models.CharField(choices=[('0', '0+'), ('6', '6+'), ('12', '12+'), ('16', '16+'), ('18', '18+')], default='0', max_length=3, verbose_name='Возрастные ограничения')),
                ('book_amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Количество книг в наличии')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True, editable=False)),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Рейтинг')),
                ('author', models.ManyToManyField(to='handbook.Author', verbose_name='Автор/Авторы книги')),
                ('genre', models.ManyToManyField(to='handbook.BookGenre', verbose_name='Жанр/Жанры книги')),
                ('publishing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='handbook.publishinghouse', verbose_name='Издательство')),
                ('seria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='handbook.bookseria', verbose_name='Серия книги')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=20, verbose_name='Логин')),
                ('books', models.ManyToManyField(to='book.Book', verbose_name='Книги')),
            ],
        ),
    ]
