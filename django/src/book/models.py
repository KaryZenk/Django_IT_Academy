from django.db import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///book_store.sqlite', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Название книги
# Фото обложки
# Цена (BYN)
# Авторы книги (может содержать несколько авторов) - справочник
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


class Book(models.Model):
    book_name = models.CharField(
    "Название Книги",
    max_length="50",
    blank=False,
    null=False
    )