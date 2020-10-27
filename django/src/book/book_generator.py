from . import models
import random
from book.dictionary import library, genres, publishers
from handbook import models as handbook_models

def generate():
    for book_name in list(library)*3:
        author_names = library[book_name]
        authors = []
        for author_name in author_names:
            author, _ = handbook_models.Author.objects.get_or_create(name=author_name)
            author.save()
            authors.append(author)
        seria, _  = handbook_models.BookSeria.objects.get_or_create(name=f'Серия {random.randint(1, 100)}')
        seria.save()
        genre_list = []
        publisher, _ = handbook_models.PublishingHouse.objects.get_or_create(name=random.choice(publishers))
        publisher.save()
        for _ in range(random.randint(1, 2)):
            genre, _ = handbook_models.BookGenre.objects.get_or_create(name=random.choice(genres))
            genre.save()
            genre_list.append(genre)
        size = f'{random.randint(90, 400)}x{random.randint(90, 400)}/{random.randint(10, 400)}'
        book = models.Book(
            name=book_name,
            year=random.randint(1990, 2020),
            price=random.randint(2, 200),
            seria=seria,
            pages=random.randint(1, 500),
            cover=random.choice(models.TypeCover.choices),
            size=size,
            publishing=publisher,
            weight=random.randint(10, 1000),
            restrictions=random.choice(models.AgeRestictions.choices),
            book_amount=random.randint(0, 100)
        )
        book.save()
        book.authors.add(*authors)
        book.genres.add(*genre_list)
        book.save()
