from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, BookGenre, BookSeria, PublishingHouse

def show_references_view(request):
    """Return a list of References obj"""
    genres = BookGenre.objects.all() 
    con = {'genre_keys': genres}
    return render(request, template_name='handbook/ref_list.html', context=con)

def show_genre_by_pk_view(request, genre_id):
    # /genre/1,2,3
    genre_obj = BookGenre.objects.get(pk=genre_id)
    con = {'genre': genre_obj}
    return render(request, template_name='handbook/genre.html', context=con)
