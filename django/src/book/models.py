from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


class TypeCover(models.TextChoices):
    HARDCOVER = 'HC', 'Твёрдый переплёт'
    SOFTCOVER = 'SC', 'Мягкая обложка'


class AgeRestictions(models.TextChoices):
    ZERO = '0', '0+'
    SIX = '6', '6+'
    TWELVE = '12', '12+'
    SIXTEEN = '16', '16+'
    EIGHTEEN = '18', '18+'


class Book(models.Model):
    name = models.CharField(
        "Название Книги",
        max_length=100,
        blank=False,
        null=False
    )
    photo = models.ImageField(
        verbose_name='Фото обложки',
        upload_to='media/',
        height_field=100,
        width_field=100,
        blank=True,
        null=True
    )
    author = models.ManyToManyField(
        'handbook.Author',
        verbose_name='Автор/Авторы книги'    
    )
    price = models.DecimalField(
        verbose_name='Цена (BYN)',
        default=0,
        max_digits=10,
        decimal_places=2
    )
    year = models.IntegerField(
        verbose_name='Год издания',
        validators=[MaxValueValidator(3000), MinValueValidator(0)]
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
    pages = models.IntegerField(
        verbose_name='Кол-во страницы',
        validators=[MinValueValidator(1)]
    )
    cover = models.CharField(
        verbose_name='Переплёт',
        max_length=2,
        choices=TypeCover.choices,
        default=TypeCover.HARDCOVER,
    )
    size = models.CharField(
        verbose_name='Формат',
        max_length=50,
        validators=[RegexValidator(
            regex=r'\d{2,3}x\d{2,3}/\d{2,3}',
            message='Формат: 120x80/32'
        )],
        blank=True,
        null=True
    )
    isbn = models.CharField(
        verbose_name='ISBN',
        max_length=17,
        blank=True,
        null=True
    )
    weight = models.IntegerField(
        verbose_name='Вес (гр.)',
        blank=True,
        null=True
    )
    restrictions = models.CharField(
        verbose_name='Возрастные ограничения',
        max_length=3,
        choices=AgeRestictions.choices,
        default=AgeRestictions.ZERO
    )
    book_amount = models.IntegerField(
        verbose_name='Количество книг в наличии',
        validators=[MinValueValidator(0)]
    )
    created_at = models.DateTimeField(
        editable=False,
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        editable=False,
        auto_now=True
    )
    available = models.BooleanField(
        editable=False,
        default=True
    )
    rating = models.FloatField(
        verbose_name='Рейтинг',
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        default=0
    )

    def __str__(self):
        return (f'{self.name} {self.photo.name} {self.price} {self.author.name} '
                f'{self.year} {self.seria.name} {self.genre.name} {self.publishing.name} {self.cover}'
                f'{self.size} {self.isbn} {self.weight} {self.restrictions} {self.book_amount} {self.created_at}'
                f'{self.modified_at} {self.available} {self.rating}')


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