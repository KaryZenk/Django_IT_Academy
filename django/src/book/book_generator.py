from . import models
import random

AUTHORS = ['Author 1', 'Authtor 2', 'Authtor 3']
BOOKS = ['Book 1', 'Book 2', 'Book 3']


def generate():
    for i in range(300):
        authors = []
        for _ in range(random.randint(1, 3)):
            author = models.Author(name=random.choice(AUTHORS))
            author.save()
            authors.append(author)
        book = models.Book(name=random.choice(BOOKS), author=author)  # TODO: Pass authors
        book.save()
