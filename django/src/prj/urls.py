"""prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path


from hello_world.views import hello_world
from book.views import book, generate_books

from handbook.views import show_genres_view, show_genre_by_pk_view, show_authors_view, show_author_by_pk_view, show_publishers_view
from handbook.views import show_publisher_by_pk_view, show_series_view, show_seria_by_pk_view, show_books_view, show_book_by_pk_view
from handbook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', hello_world),
    path('generate/', generate_books),
    path('genre/<int:genre_id>/', show_genre_by_pk_view),
    path('genre/create/', views.create_genre_view),
    path('genre/update/<int:pk>/', views.update_genre_view),
    path('genre/delete/<int:pk>/', views.delete_genre_view),
    path('genre/', show_genres_view),
    path('author/', show_authors_view),
    path('author/<int:author_id>/', show_author_by_pk_view),
    path('author/create/', views.create_author_view),
    path('author/update/<int:pk>/', views.update_author_view),
    path('author/delete/<int:pk>/', views.delete_author_view),
    path('publisher/', show_publishers_view),
    path('publisher/<int:publisher_id>/', show_publisher_by_pk_view),
    path('publisher/create/', views.create_publisher_view),
    path('publisher/update/<int:pk>/', views.update_publisher_view),
    path('publisher/delete/<int:pk>/', views.delete_publisher_view),
    path('seria/', show_series_view),
    path('seria/<int:seria_id>/', show_seria_by_pk_view),
    path('seria/create/', views.create_seria_view),
    path('seria/update/<int:pk>/', views.update_seria_view),
    path('seria/delete/<int:pk>/', views.delete_seria_view),
    path('book/', show_books_view),
    path('book/<int:book_id>/', show_book_by_pk_view),
    path('book/create/', views.create_book_view),
    path('book/update/<int:pk>/', views.update_book_view),
    path('book/delete/<int:pk>/', views.delete_book_view),
]
