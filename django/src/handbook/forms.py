from django import forms

from . import models
from book import models as book_models

class CreateGenreForm(forms.Form):
    name = forms.CharField(max_length=40, required=True)

class UpdateGenreForm(forms.Form):
    name = forms.CharField(max_length=40, required=True)
    pk = forms.CharField(widget=forms.HiddenInput)


class CreateAuthorForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)

class UpdateAuthorForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    pk = forms.CharField(widget=forms.HiddenInput)


class CreatePublisherForm(forms.Form):
    name = forms.CharField(max_length=40, required=True)

class UpdatePublisherForm(forms.Form):
    name = forms.CharField(max_length=40, required=True)
    pk = forms.CharField(widget=forms.HiddenInput)


class CreateSeriaForm(forms.Form):
    name = forms.CharField(max_length=40, required=True)

class UpdateSeriaForm(forms.Form):
    name = forms.CharField(max_length=40, required=True)
    pk = forms.CharField(widget=forms.HiddenInput)


class CreateBookForm(forms.ModelForm):
    # authors = forms.CharField()
    class Meta:
        model = book_models.Book
        fields = '__all__'

class UpdateBookForm(forms.ModelForm):
    # authors = forms.CharField()
    class Meta:
        model = book_models.Book
        fields = '__all__'