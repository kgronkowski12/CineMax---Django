from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/genre/',views.addGenre),
    path('add/movie/',views.addMovie),
    path('add/repertuar/',views.addRepertuar),
    path('add/director/',views.addDirector ),
    path('edit/genre/<slug>',views.editGenre),
    path('edit/director/<slug>',views.editDirector),
    path('edit/movie/<slug>',views.editMovie),
    path('edit/repertuar/<slug>',views.editRepertuar),

    path('delete/genre/<slug>',views.deleteGenre),
    path('delete/director/<slug>',views.deleteDirector),
    path('delete/movie/<slug>',views.deleteMovie),
    path('delete/repertuar/<slug>',views.deleteRepertuar),

    path('genres/',views.showGenres),
    path('directors/',views.showDirectors),

    path('view/<slug>/',views.allMovies),
    path('watch/<slug>/',views.movie),
    path('watch/<slug>/deleteComment/<slug2>',views.deleteComment),
    path('buy/<slug>/',views.buy),
    path('director/<slug>/',views.director),
    path('genre/<slug>/',views.genre),
    path('checkout/<slug1>/<slug2>/',views.checkout),
]