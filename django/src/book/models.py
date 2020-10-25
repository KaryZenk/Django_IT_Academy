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
class BookAuthor(models.Model):  # Авторы книги (может содержать несколько авторов) - справочник
    book_author = models.CharField(
        'Авторы книги',
        max_length=50
    )
    description = models.TextField(
        'Авторы книги из справочника',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.book_author

class Book(models.Model):  # Название книги
    book_name = models.CharField(
        "Название Книги",
        max_length=100,
        blank=False,  #Обязательно к заполнению, пустым не может быть
        null=False  
    )
    book_author = models.ForeignKey(
        BookAuthor,
        on_delete=models.PROTECT    
    )

    #user 

    def __str__(self):
        return f'{self.book_name} {self.book_author.book_author}'

