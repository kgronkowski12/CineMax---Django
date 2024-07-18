from django.db import models

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50,verbose_name='Nazwa')
    desc = models.CharField(max_length=500,verbose_name='Opis')
    def __str__(self):
        return self.name
    def get_link(self):
        return("genre/"+str(self.id))
    def edit_link(self):
        return("edit/genre/"+str(self.id))
    def delete_link(self):
        return("delete/genre/"+str(self.id))

class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50,verbose_name='Imie')
    desc = models.CharField(max_length=500,verbose_name='Opis')
    def __str__(self):
        return self.name
    def get_link(self):
        return("director/"+str(self.id))
    def edit_link(self):
        return("edit/director/"+str(self.id))
    def delete_link(self):
        return("delete/director/"+str(self.id))

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    img_name = models.CharField(max_length=50,verbose_name='Nazwa pliku .png')
    name = models.CharField(max_length=50,verbose_name='Nazwa filmu')
    description = models.CharField(max_length=500,verbose_name='Opis')
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE,default=0,verbose_name='Gatunek')
    director_id = models.ForeignKey(Director, on_delete=models.CASCADE,default=0,verbose_name='Reżyser')
    pub_date = models.DateField('Data wydania')
    def get_movie_link(self):
        return("watch/"+str(self.id))
    def get_director_link(self):
        return("director/"+str(self.director_id.id))
    def get_genre_link(self):
        return("genre/"+str(self.genre_id.id))
    def edit_link(self):
        return("edit/movie/"+str(self.id))
    def delete_link(self):
        return("delete/movie/"+str(self.id))
    def __str__(self):
        return self.name

class Repertoire(models.Model):
    id = models.IntegerField(primary_key=True)
    #movie_id = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE,verbose_name='Grany film')
    start_time = models.DateTimeField(verbose_name='Początek seansu')
    end_time = models.DateTimeField(verbose_name='Koniec seansu')
    price = models.IntegerField(verbose_name='Cena biletu')
    def edit_link(self):
        return("edit/repertuar/"+str(self.id))
    def delete_link(self):
        return("delete/repertuar/"+str(self.id))
    def buy_link(self):
        return("buy/"+str(self.id))

class Comment(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    score = models.IntegerField()
    comment = models.CharField(max_length=500)


class Ticket(models.Model):
    seat_nr = models.IntegerField()
    movie_id = models.ForeignKey(Repertoire, on_delete=models.CASCADE)

class Staff(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
