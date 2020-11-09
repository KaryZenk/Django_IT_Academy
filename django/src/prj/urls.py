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
from handbook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello_world/', hello_world),
    path('generate/', generate_books),

    path('genre/<int:pk>/', views.ShowGenreView.as_view()),
    path('genre/createview/', views.CreateGenreView.as_view()),
    path('genre/updateview/<int:pk>/', views.UpdateGenreView.as_view()),
    path('genre/deleteview/<int:pk>/', views.DeleteGenreView.as_view()),
    path('genre/', views.ShowGenresView.as_view()),

    path('author/', views.ShowAuthorsView.as_view()),
    path('author/<int:pk>/', views.ShowAuthorView.as_view()),
    path('author/createview/', views.CreateAuthorView.as_view()),
    path('author/updateview/<int:pk>/', views.UpdateAuthorView.as_view()),
    path('author/deleteview/<int:pk>/', views.DeleteAuthorView.as_view()),

    path('publisher/', views.ShowPublishersView.as_view()),
    path('publisher/<int:pk>/', views.ShowPublisherView.as_view()),
    path('publisher/createview/', views.CreatePublisherView.as_view()),
    path('publisher/updateview/<int:pk>/', views.UpdatePublisherView.as_view()),
    path('publisher/deleteview/<int:pk>/', views.DeletePublisherView.as_view()),

    path('seria/', views.ShowSeriasView.as_view()),
    path('seria/<int:pk>/', views.ShowSeriaView.as_view()),
    path('seria/createview/', views.CreateSeriaView.as_view()),
    path('seria/updateview/<int:pk>/', views.UpdateSeriaView.as_view()),
    path('seria/deleteview/<int:pk>/', views.DeleteSeriaView.as_view()),
    
    path('book/<int:pk>/', views.ShowBookView.as_view()),
    path('book/createview/', views.CreateBookView.as_view()),
    path('book/updateview/<int:pk>/', views.UpdateBookView.as_view()),
    path('book/deleteview/<int:pk>/', views.DeleteBookView.as_view()),
    path('', views.ShowBooksView.as_view()),

]
