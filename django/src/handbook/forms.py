from django import forms

from . import models
from book import models as book_models


class CreateGenreForm(forms.ModelForm):
    class Meta:
        model = models.BookGenre
        fields = '__all__'

class UpdateGenreForm(forms.ModelForm):
    class Meta:
        model = models.BookGenre
        fields = '__all__'


class CreateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'

class UpdateAuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = '__all__'


class CreatePublisherForm(forms.ModelForm):
    class Meta:
        model = models.PublishingHouse
        fields = '__all__'

class UpdatePublisherForm(forms.ModelForm):
    class Meta:
        model = models.PublishingHouse
        fields = '__all__'


class CreateSeriaForm(forms.ModelForm):
    class Meta:
        model = models.BookSeria
        fields = '__all__'

class UpdateSeriaForm(forms.ModelForm):
    class Meta:
        model = models.BookSeria
        fields = '__all__'


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = book_models.Book
        fields = '__all__'

class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = book_models.Book
        fields = '__all__'