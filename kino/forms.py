from django import forms  #biblioteka forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import RegexValidator
from .models import *
from django.forms import ModelForm

class OpinionForm(forms.Form):
    #widget = forms.HiddenInput()
    #movieId = forms.CharField(widget = forms.HiddenInput())
    score = forms.IntegerField(label='Score',validators=[MinValueValidator(0),MaxValueValidator(10)])
    comment = forms.CharField(widget=forms.Textarea,label='Recenzja', max_length=100) 

class BuyForm(forms.Form):
    #widget = forms.HiddenInput()
    seatnr = forms.CharField(widget = forms.HiddenInput())
    imie = forms.CharField(label='Imie', max_length=100)
    nazwisko = forms.CharField(label='Nazwisko', max_length=100)
    email = forms.EmailField(label='Adres Email', max_length=100)
    nrKarty = forms.CharField(label='Karta', max_length=16, min_length=9, validators=[RegexValidator(r'^\d{1,17}$')])
    kodCvv = forms.CharField(label='Kod CVV', max_length=4, min_length=3, validators=[RegexValidator(r'^\d{1,10}$')])

class GenreForm(forms.Form):
    nazwa = forms.CharField(label='Nazwa', max_length=100)
    opis = forms.CharField(label='Opis', max_length=500)


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        exclude = ('id',)


class DirectorForm(ModelForm):
    class Meta:
        model = Director
        exclude = ('id',)

class RepertuarForm(ModelForm):
    class Meta:
        model = Repertoire
        exclude = ('id',)