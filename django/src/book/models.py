from django.db import models
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy import Column, Integer, String
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///book_store.sqlite', echo=False)
# Session = sessionmaker(bind=engine)
# session = Session()
# Base = declarative_base()

# Фото обложки
# Цена (BYN)
# Серия - справочник
# Жанры (один или несколько жанров) - справочник
# Год издания
# Страниц
# Переплет
# Формат
# ISBN
# Вес (гр)
# Возрастные ограничения
# Издательство - справочник
# Количество книг в наличии
# Активный (доступен для заказа, Да/Нет)
# Рейтинг (0 - 10)
# Дата внесения в каталог
# Дата последнего изменения карточки


# Пароль
# E-mail
# Имя
# Фамилия
# Телефон
# Группа - недоступно для редактирования. Принадлежность присваивается автоматически
# Домашний адрес
# Страна
# Город
# Индекс
# Адрес1
# Адрес2
# Дополнительная информация


class Author(models.Model):  # Авторы книги (может содержать несколько авторов) - справочник
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


class Book(models.Model):  # Название книги
    name = models.CharField(
        "Название Книги",
        max_length=100,
        blank=False,  #Обязательно к заполнению, пустым не может быть
        null=False  
    )
    author = models.ForeignKey(
        Author,
        verbose_name='Автор/Авторы книги',
        on_delete=models.PROTECT    
    )

    def __str__(self):
        return f'{self.name} {self.author.name}'


class Byer(models.Model):  #Профиль покупателя
    login = models.CharField(  # Логин
        "Логин",
        max_length=20,
    )
    books = models.ManyToManyField(
        Book,
        verbose_name='Книги'
    )

    def __str__(self):
        return self.login