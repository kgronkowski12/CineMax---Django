from django.conf import settings
from django.shortcuts import render
from datetime import datetime    
from django.http import HttpResponse

from .models import *

from django.core.paginator import Paginator

from django.views.generic import ListView

from django.shortcuts import render, get_object_or_404

from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from django.forms.models import model_to_dict
from .forms import *

from .combination import *

def showDirectors(request):
	allDir = Director.objects.all()
	context = {"Directors":allDir}
	return render(request, 'kino/directors.html', context)

def showGenres(request):
	allGen = Genre.objects.all()
	context = {"Genres":allGen}
	return render(request, 'kino/genres.html', context)

def deleteRepertuar(request, slug):
	rep = Repertoire.objects.filter(id=int(slug))
	rep.delete()
	context = {"komunikat":"Element repertuaru został usunięty"}
	return render(request, 'kino/komunikat.html', context)

def deleteMovie(request, slug):
	mov = Movie.objects.filter(id=int(slug))
	mov.delete()
	context = {"komunikat":"Film został usunięty"}
	return render(request, 'kino/komunikat.html', context)

def deleteGenre(request, slug):
	gen = Genre.objects.filter(id=int(slug))
	gen.delete()
	context = {"komunikat":"Gatunek został usunięty"}
	return render(request, 'kino/komunikat.html', context)

def deleteDirector(request, slug):
	director = Director.objects.filter(id=int(slug))
	director.delete()
	context = {"komunikat":"Reżyser został usunięty"}
	return render(request, 'kino/komunikat.html', context)

def addRepertuar(request):
	if request.method == 'POST':
		form = RepertuarForm(request.POST)
		if form.is_valid():
			newMovie = form.save()
	else:
		form = RepertuarForm()
		form.fields["start_time"].initial = datetime.now()
		form.fields["end_time"].initial = datetime.now()
	context = {"form":form,"name":"Dodaj","admin":True,"dodawane":"Dodaj element repertuaru"}
	return render(request, 'kino/addSm.html', context)

def editRepertuar(request, slug):
	edited = Repertoire.objects.get(id=int(slug))
	edited = model_to_dict(edited)
	if request.method == 'POST':
		form = RepertuarForm(request.POST)
		if form.is_valid():
			newMovie = form.save(commit=False)
			newMovie.id = int(slug)
			newMovie.save()
	else:
		form = RepertuarForm()
		for field in form.fields:
			form.fields[field].initial = edited[field]
	context = {"form":form,"name":"Edytuj","admin":True,"dodawane":"Edytuj element repertuaru"}
	return render(request, 'kino/addSm.html', context)

def addDirector(request):
	if request.method == 'POST':
		form = DirectorForm(request.POST)
		if form.is_valid():
			newDirector = form.save()
	else:
		form = DirectorForm()
	context = {"form":form,"name":"Dodaj","admin":True,"dodawane":"Dodaj reżysera"}
	return render(request, 'kino/addSm.html', context)

def editDirector(request, slug):
	edited = Director.objects.get(id=int(slug))
	edited = model_to_dict(edited)
	if request.method == 'POST':
		form = DirectorForm(request.POST)
		if form.is_valid():
			newDirector = form.save(commit=False)
			newDirector.id = int(slug)
			newDirector.save()
	else:
		form = DirectorForm()
		for field in form.fields:
			form.fields[field].initial = edited[field]
	context = {"form":form,"name":"Edytuj","admin":True,"dodawane":"Edytuj reżysera"}
	return render(request, 'kino/addSm.html', context)

def addMovie(request):
	if request.method == 'POST':
		form = MovieForm(request.POST)
		if form.is_valid():
			newMovie = form.save()
	else:
		form = MovieForm()
		form.fields["pub_date"].initial = datetime.now().date
	context = {"form":form,"name":"Dodaj","admin":True,"dodawane":"Dodaj film"}
	return render(request, 'kino/addSm.html', context)

def editMovie(request, slug):
	edited = Movie.objects.get(id=int(slug))
	edited = model_to_dict(edited)
	if request.method == 'POST':
		form = MovieForm(request.POST)
		if form.is_valid():
			newMovie = form.save(commit=False)
			newMovie.id = int(slug)
			newMovie.save()
	else:
		form = MovieForm()
		for field in form.fields:
			form.fields[field].initial = edited[field]
	context = {"form":form,"name":"Edytuj","admin":True,"dodawane":"Edytuj film"}
	return render(request, 'kino/addSm.html', context)

def addGenre(request):
	if request.method == 'POST':
		form = GenreForm(request.POST)
		if form.is_valid():
			newGenre = Genre()
			newGenre.name=form.cleaned_data['nazwa']
			newGenre.desc=form.cleaned_data['opis']
			newGenre.save()
	else:
		form = GenreForm()
	context = {"form":form,"name":"Dodaj","admin":True,"dodawane":"Dodaj gatunek"}
	return render(request, 'kino/addSm.html', context)

def editGenre(request, slug):
	edit = Genre.objects.get(id=int(slug))
	if request.method == 'POST':
		form = GenreForm(request.POST)
		if form.is_valid():
			newGenre = Genre()
			newGenre.id = int(slug)
			newGenre.name=form.cleaned_data['nazwa']
			newGenre.desc=form.cleaned_data['opis']
			newGenre.save()
	else:
		form = GenreForm()
		form.fields["nazwa"].initial = edit.name
		form.fields["opis"].initial = edit.desc
	context = {"form":form,"name":"Edytuj","admin":True,"dodawane":"Edytuj gatunek"}
	return render(request, 'kino/addSm.html', context)

def deleteComment(request, slug,slug2):
	if not request.user.is_authenticated or request.user.username != "admin":
		context = {"komunikat":"Nie masz uprawnień administratora!"}
		return render(request, 'kino/komunikat.html', context)
	comm = Comment.objects.filter(id=int(slug2))
	comm.delete()
	context = {}
	return redirect('../')

def genre(request, slug):
	genre = Genre.objects.get(id=int(slug))
	allMov = Movie.objects.all()
	ScorMov = []
	for x in range(len(allMov)):
		scor = ScorMovObject(allMov[x])
		ScorMov.append(scor)
	allCom = Comment.objects.all()
	for x in range(len(allCom)):
		if(allCom[x].movie_id.id<len(ScorMov)):
			ScorMov[allCom[x].movie_id.id].score+=allCom[x].score
			ScorMov[allCom[x].movie_id.id].divider+=1
	for x in range(len(ScorMov)):
		ScorMov[x].calcScore()
	ScorMov = [x for x in ScorMov if x.movie.genre_id==genre]
	context = {'Movies':ScorMov,'Genre':genre}
	return render(request, 'kino/genre.html', context)

def director(request, slug):
	director = Director.objects.get(id=int(slug))
	allMov = Movie.objects.all()
	ScorMov = []
	for x in range(len(allMov)):
		scor = ScorMovObject(allMov[x])
		ScorMov.append(scor)
	allCom = Comment.objects.all()
	for x in range(len(allCom)):
		ScorMov[allCom[x].movie_id.id].score+=allCom[x].score
		ScorMov[allCom[x].movie_id.id].divider+=1
	for x in range(len(ScorMov)):
		ScorMov[x].calcScore()
	ScorMov = [x for x in ScorMov if x.movie.director_id==director]
	context = {'Movies':ScorMov,'Director':director}
	return render(request, 'kino/director.html', context)

def movie(request, slug):
	comments = []
	searched = Movie.objects.filter(id=int(slug))
	allCom = Comment.objects.all()
	points = 0
	pointDiviser=0
	isAdmin = False
	yourcomment = None
	if request.user.is_authenticated:
		if request.user.username == "admin":
			isAdmin=True
	for x in range(len(allCom)):
		if allCom[x].movie_id.id==int(slug):
			comments.append(allCom[x])
			if request.user.is_authenticated:
				if allCom[x].name == request.user.username:
					yourcomment = allCom[x]
			print("+")
			points+=allCom[x].score
			pointDiviser+=1
	if pointDiviser>0:
		points/=pointDiviser
	points = round(points,2)
	context = {}

	if request.method == 'POST':
    	# create a form instance and populate it with data from the request:
		form = OpinionForm(request.POST)
		if form.is_valid():
			if yourcomment==None:
				newComment = Comment()
				newComment.movie_id=Movie.objects.get(id=int(slug))
				print(newComment.id)
				newComment.name=request.user.username
				newComment.score=form.cleaned_data['score']
				newComment.comment=form.cleaned_data['comment']
				newComment.save()
				context = {"komunikat":"Dziękujemy za dodanie recenzji!"}
				return render(request, 'kino/komunikat.html', context)
			elif request.POST.get("edit"):
				yourcomment.score=form.cleaned_data['score']
				yourcomment.comment=form.cleaned_data['comment']
				yourcomment.save()
				context = {"komunikat":"Twoja recenzja została zedytowana."}
				return render(request, 'kino/komunikat.html', context)
			else:
				yourcomment.delete()
				context = {"komunikat":"Twoja recenzja została usunięta."}
				return render(request, 'kino/komunikat.html', context)
				

	else:
		form = OpinionForm()
		if yourcomment!=None:
			form.fields["score"].initial=yourcomment.score
			form.fields["comment"].initial=yourcomment.comment

	if yourcomment!=None:
		yourcomment=True
	else:
		yourcomment=False
	context = {'Movies':searched,'Comments':comments,"form":form,"points":points,"yourComment":yourcomment,"isAdmin":isAdmin}
	return render(request, 'kino/movie.html', context)


def allMovies(request, slug):
	isAdmin = False
	if request.user.is_authenticated:
		if request.user.username == "admin":
			isAdmin=True
	allMov=Movie.objects.all()
	ScorMov = []
	for x in range(len(allMov)):
		scor = ScorMovObject(allMov[x])
		ScorMov.append(scor)
	allCom = Comment.objects.all()
	for x in range(len(allCom)):
		ScorMov[allCom[x].movie_id.id].score+=allCom[x].score
		ScorMov[allCom[x].movie_id.id].divider+=1
	for x in range(len(ScorMov)):
		ScorMov[x].calcScore()
	if int(slug)==0:
		ScorMov= sorted(ScorMov,key=lambda x: x.movie.name)
	elif int(slug)==1:
		ScorMov = sorted(ScorMov,key=lambda x: x.movie.pub_date)
	elif int(slug)==2:
		ScorMov = sorted(ScorMov,key=lambda x: x.score, reverse=True)
	elif int(slug)==3:
		ScorMov = sorted(ScorMov,key=lambda x: x.movie.genre_id.name)
	context = {'Movies':ScorMov,'admin':isAdmin}
	return render(request, 'kino/allmovies.html', context)

def checkout(request, slug1, slug2):
	if request.method == 'POST':
    	# create a form instance and populate it with data from the request:
		form = BuyForm(request.POST)
		if form.is_valid():
			newTicket = Ticket()
			newTicket.movie_id=Repertoire.objects.get(id=int(slug1))
			newTicket.seat_nr=form.cleaned_data['seatnr']
			newTicket.save()
			context = {"komunikat":"Bilet został zakupiony."}
			return render(request, 'kino/komunikat.html', context)
	else:
		form = BuyForm()
		form.fields['seatnr'].initial = int(slug2)

	context = {"form":form}
	return render(request, 'kino/checkout.html', context)

def index(request):
	isAdmin = False
	if request.user.is_authenticated:
		if request.user.username == "admin":
			isAdmin=True
	allRep=Repertoire.objects.all()
	allRep=sorted(allRep,key=lambda x : x.start_time)
	#context = {'Movies':Repertoire.objects.all()}
	context = {'Movies':allRep,"admin":isAdmin}
	return render(request, 'kino/repertuar.html', context)

def err(request):
	context = {}
	return render(request, 'kino/404.html', context)

def buy(request, slug):
	allMov=Repertoire.objects.all()
	for x in range(len(allMov)):
		if allMov[x].id==int(slug):
			break
		elif x==len(allMov)-1:
			return err(request)
	allTick=Ticket.objects.all()
	seats = []
	for x in range(5):
		row = []
		for y in range(5):
			seat = tickAccess(x*5+y+1)
			seat.rownr=x+1
			row.append(seat)
		seats.append(row)
	
	for x in range(len(allTick)):
		if allTick[x].movie_id.id==int(slug):
			seats[int(allTick[x].seat_nr/5)][allTick[x].seat_nr%5-1].access="navb"

	context = {'rows':seats,'mov':int(slug)}
	return render(request, 'kino/buy.html', context)
