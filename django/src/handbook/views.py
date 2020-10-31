from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Author, BookGenre, BookSeria, PublishingHouse

from .forms import CreateGenreForm, UpdateGenreForm, CreateAuthorForm, UpdateAuthorForm, CreatePublisherForm, UpdatePublisherForm
from .forms import CreateSeriaForm, UpdateSeriaForm

# Wrong, but it is still working

def show_genres_view(request):
    """Return a list of References obj"""
    genres = BookGenre.objects.all() 
    con = {'genre_keys': genres}
    return render(request, template_name='handbook/genre_list.html', context=con)

def show_genre_by_pk_view(request, genre_id):
    # /genre/1,2,3
    genre_obj = BookGenre.objects.get(pk=genre_id)
    con = {'genre': genre_obj}
    return render(request, template_name='handbook/genre.html', context=con)

def create_genre_view(request):
    if request.method == 'POST':
        form = CreateGenreForm(data=request.POST)
        if form.is_valid():
            genre_name = form.cleaned_data.get('name')
            BookGenre.objects.create(name=genre_name)
            return HttpResponseRedirect('/genre/')
    else:
        form = CreateGenreForm()
    return render(
        request,
        template_name='handbook/create_genre.html', 
        context={'form': form})
   
def update_genre_view(request, pk):
    if request.method == 'POST':
        form = UpdateGenreForm(data=request.POST)
        if form.is_valid():
            genre_name = form.cleaned_data.get('name')
            form_pk = form.cleaned_data.get('pk')
            obj = BookGenre.objects.get(pk=form_pk)
            obj.name = genre_name
            obj.save()
            return HttpResponseRedirect('/genre/')
    else:
        genre = BookGenre.objects.get(pk=pk)
        form = UpdateGenreForm(data={'name': genre.name, 'pk': genre.pk})
    return render(
        request,
        template_name='handbook/create_genre.html', 
        context={'form': form})
   
def delete_genre_view(request, pk):
    if request.method == 'POST':
        genre = BookGenre.objects.filter(pk=pk).delete()
        return HttpResponseRedirect('/genre/')
    else:
        genre = BookGenre.objects.get(pk=pk)
    return render(
        request,
        template_name='handbook/delete_genre.html', 
        context={'genre': genre})


def show_authors_view(request):
    authors = Author.objects.all() 
    con = {'author_keys': authors}
    return render(request, template_name='handbook/author_list.html', context=con)

def show_author_by_pk_view(request, author_id):
    author_obj = Author.objects.get(pk=author_id)
    con = {'author': author_obj}
    return render(request, template_name='handbook/author.html', context=con)

def create_author_view(request):
    if request.method == 'POST':
        form = CreateAuthorForm(data=request.POST)
        if form.is_valid():
            author_name = form.cleaned_data.get('name')
            Author.objects.create(name=author_name)
            return HttpResponseRedirect('/author/')
    else:
        form = CreateAuthorForm()
    return render(
        request,
        template_name='handbook/create_author.html', 
        context={'form': form})

def update_author_view(request, pk):
    if request.method == 'POST':
        form = UpdateAuthorForm(data=request.POST)
        if form.is_valid():
            author_name = form.cleaned_data.get('name')
            form_pk = form.cleaned_data.get('pk')
            obj = Author.objects.get(pk=form_pk)
            obj.name = author_name
            obj.save()
            return HttpResponseRedirect('/author/')
    else:
        author = Author.objects.get(pk=pk)
        form = UpdateAuthorForm(data={'name': author.name, 'pk': author.pk})
    return render(
        request,
        template_name='handbook/create_author.html', 
        context={'form': form})

def delete_author_view(request, pk):
    if request.method == 'POST':
        author = Author.objects.filter(pk=pk).delete()
        return HttpResponseRedirect('/author/')
    else:
        author = Author.objects.get(pk=pk)
    return render(
        request,
        template_name='handbook/delete_author.html', 
        context={'author': author})


def show_publishers_view(request):
    publishers = PublishingHouse.objects.all() 
    con = {'publisher_keys': publishers}
    return render(request, template_name='handbook/publisher_list.html', context=con)

def show_publisher_by_pk_view(request, publisher_id):
    # /publisher/1,2,3
    publisher_obj = PublishingHouse.objects.get(pk=publisher_id)
    con = {'publisher': publisher_obj}
    return render(request, template_name='handbook/publisher.html', context=con)

def create_publisher_view(request):
    if request.method == 'POST':
        form = CreatePublisherForm(data=request.POST)
        if form.is_valid():
            publisher_name = form.cleaned_data.get('name')
            PublishingHouse.objects.create(name=publisher_name)
            return HttpResponseRedirect('/publisher/')
    else:
        form = CreatePublisherForm()
    return render(
        request,
        template_name='handbook/create_publisher.html', 
        context={'form': form})

def update_publisher_view(request, pk):
    if request.method == 'POST':
        form = UpdatePublisherForm(data=request.POST)
        if form.is_valid():
            publisher_name = form.cleaned_data.get('name')
            form_pk = form.cleaned_data.get('pk')
            obj = PublishingHouse.objects.get(pk=form_pk)
            obj.name = publisher_name
            obj.save()
            return HttpResponseRedirect('/publisher/')
    else:
        publisher = PublishingHouse.objects.get(pk=pk)
        form = UpdatePublisherForm(data={'name': publisher.name, 'pk': publisher.pk})
    return render(
        request,
        template_name='handbook/create_publisher.html', 
        context={'form': form})

def delete_publisher_view(request, pk):
    if request.method == 'POST':
        publisher = PublishingHouse.objects.filter(pk=pk).delete()
        return HttpResponseRedirect('/publisher/')
    else:
        publisher = PublishingHouse.objects.get(pk=pk)
    return render(
        request,
        template_name='handbook/delete_publisher.html', 
        context={'publisher': publisher})


def show_series_view(request):
    series = BookSeria.objects.all() 
    con = {'seria_keys': series}
    return render(request, template_name='handbook/seria_list.html', context=con)

def show_seria_by_pk_view(request, seria_id):
    # /seria/1,2,3
    seria_obj = BookSeria.objects.get(pk=seria_id)
    con = {'seria': seria_obj}
    return render(request, template_name='handbook/seria.html', context=con)

def create_seria_view(request):
    if request.method == 'POST':
        form = CreateSeriaForm(data=request.POST)
        if form.is_valid():
            seria_name = form.cleaned_data.get('name')
            BookSeria.objects.create(name=seria_name)
            return HttpResponseRedirect('/seria/')
    else:
        form = CreateSeriaForm()
    return render(
        request,
        template_name='handbook/create_seria.html', 
        context={'form': form})

def update_seria_view(request, pk):
    if request.method == 'POST':
        form = UpdateSeriaForm(data=request.POST)
        if form.is_valid():
            seria_name = form.cleaned_data.get('name')
            form_pk = form.cleaned_data.get('pk')
            obj = BookSeria.objects.get(pk=form_pk)
            obj.name = seria_name
            obj.save()
            return HttpResponseRedirect('/seria/')
    else:
        seria = BookSeria.objects.get(pk=pk)
        form = UpdateSeriaForm(data={'name': seria.name, 'pk':seria.pk})
    return render(
        request,
        template_name='handbook/create_seria.html', 
        context={'form': form})

def delete_seria_view(request, pk):
    if request.method == 'POST':
        seria = BookSeria.objects.filter(pk=pk).delete()
        return HttpResponseRedirect('/seria/')
    else:
        seria = BookSeria.objects.get(pk=pk)
    return render(
        request,
        template_name='handbook/delete_seria.html', 
        context={'seria': seria})