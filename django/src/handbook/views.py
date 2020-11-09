from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Author, BookGenre, BookSeria, PublishingHouse

from .forms import CreateGenreForm, UpdateGenreForm, CreateAuthorForm, UpdateAuthorForm, CreatePublisherForm, UpdatePublisherForm
from .forms import CreateSeriaForm, UpdateSeriaForm, CreateBookForm, UpdateBookForm

from book.models import Book, AgeRestictions, TypeCover


class ShowBooksView(ListView):
    template_name='handbook/book_list.html'
    model = Book

class ShowBookView(DetailView):
    template_name = 'handbook/book.html'
    model = Book

class CreateBookView(CreateView):
    template_name = 'handbook/create_book.html'
    model = Book
    form_class = CreateBookForm
    success_url='/'

class UpdateBookView(UpdateView):
    template_name = 'handbook/update_book.html'
    model = Book
    form_class = UpdateBookForm
    success_url='/'

class DeleteBookView(DeleteView):
    template_name = 'handbook/delete_book.html'
    model = Book
    success_url='/'


class ShowGenresView(ListView):
    template_name='handbook/genre_list.html'
    model = BookGenre

class ShowGenreView(DetailView):
    template_name = 'handbook/genre.html'
    model = BookGenre

class CreateGenreView(CreateView):
    template_name = 'handbook/create_genre.html'
    model = BookGenre
    form_class = CreateGenreForm
    success_url='/genre/'
   
class UpdateGenreView(UpdateView):
    template_name = 'handbook/create_genre.html'
    model = BookGenre
    form_class = UpdateGenreForm
    success_url='/genre/'
   
class DeleteGenreView(DeleteView):
    template_name = 'handbook/delete_genre.html'
    model = BookGenre
    success_url='/genre/'


class ShowAuthorsView(ListView):
    template_name='handbook/author_list.html'
    model = Author

class ShowAuthorView(DetailView):
    template_name = 'handbook/author.html'
    model = Author

class CreateAuthorView(CreateView):
    template_name = 'handbook/create_author.html'
    model = Author
    form_class = CreateAuthorForm
    success_url='/author/'

class UpdateAuthorView(UpdateView):
    template_name = 'handbook/create_author.html'
    model = Author
    form_class = UpdateAuthorForm
    success_url='/author/'

class DeleteAuthorView(DeleteView):
    template_name = 'handbook/delete_author.html'
    model = Author
    success_url='/author/'


class ShowPublishersView(ListView):
    template_name='handbook/publisher_list.html'
    model = PublishingHouse

class ShowPublisherView(DetailView):
    template_name = 'handbook/publisher.html'
    model = PublishingHouse

class CreatePublisherView(CreateView):
    template_name = 'handbook/create_publisher.html'
    model = PublishingHouse
    form_class = CreatePublisherForm
    success_url='/publisher/'

class UpdatePublisherView(UpdateView):
    template_name = 'handbook/create_publisher.html'
    model = PublishingHouse
    form_class = UpdatePublisherForm
    success_url='/publisher/'

class DeletePublisherView(DeleteView):
    template_name = 'handbook/delete_publisher.html'
    model = PublishingHouse
    success_url='/publisher/'


class ShowSeriasView(ListView):
    template_name='handbook/seria_list.html'
    model = BookSeria

class ShowSeriaView(DetailView):
    template_name = 'handbook/seria.html'
    model = BookSeria

class CreateSeriaView(CreateView):
    template_name = 'handbook/create_seria.html'
    model = BookSeria
    form_class = CreateSeriaForm
    success_url='/seria/'

class UpdateSeriaView(UpdateView):
    template_name = 'handbook/create_seria.html'
    model = BookSeria
    form_class = UpdateSeriaForm
    success_url='/seria/'

class DeleteSeriaView(DeleteView):
    template_name = 'handbook/delete_seria.html'
    model = BookSeria
    success_url='/seria/'
