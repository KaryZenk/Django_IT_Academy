from django.db import models

class Author(models.Model):  # Авторы книги (может содержать несколько авторов)
    name = models.CharField(
        'Автор книги',
        max_length=50
    )
    description = models.TextField(
        'Автор книги из справочника',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

class BookSeria(models.Model):  # Серия
    name = models.CharField(
        'Серия книг',
        max_length=40
    )
    description = models.TextField(
        'Описание серии книг',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

class BookGenre(models.Model):  # Жанры (один или несколько жанров
    name = models.CharField(
        'Жанр книги',
        max_length=40
    )
    description = models.TextField(
        'Описание жанра',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

class PublishingHouse(models.Model):  # Издательство
    name = models.CharField(
        'Издательство',
        max_length=40
    )

    def __str__(self):
        return self.name
