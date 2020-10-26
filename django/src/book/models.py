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
# Год издания
# Страниц
# Переплет
# Формат
# ISBN
# Вес (гр)
# Возрастные ограничения
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

class Book(models.Model):  # Название книги
    name = models.CharField(
        "Название Книги",
        max_length=100,
        blank=False,  #Обязательно к заполнению, пустым не может быть
        null=False  
    )
    author = models.ManyToManyField(
        'handbook.Author',
        verbose_name='Автор/Авторы книги'    
    )
    seria = models.ForeignKey(
        'handbook.BookSeria',
        verbose_name='Серия книги',
        on_delete=models.PROTECT
    )
    genre = models.ManyToManyField(
        'handbook.BookGenre',
        verbose_name='Жанр/Жанры книги'
    )
    publishing = models.ForeignKey(
        'handbook.PublishingHouse',
        verbose_name='Издательство',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return f'{self.name} {self.author.name} {self.seria.name} {self.genre.name} {self.publishing.name}'


class Customer(models.Model):  #Профиль покупателя
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