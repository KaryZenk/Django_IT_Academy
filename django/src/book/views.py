from django.shortcuts import render
from django.http import HttpResponse
from . import book_generator

def book(request):
    return HttpResponse("")


def generate_books(request):
    book_generator.generate()
    return HttpResponse("Generated")
