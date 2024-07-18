from .models import *

class repMov():
	def __init__(self, rep, movie):
		self.rep = rep
		self.movie = movie

	def get_movie_link(self):
		return("watch/"+str(self.movie.id))
	def buy_link(self):
		return("buy/"+str(self.rep.id))

class ScorMovObject():
	def __init__(self, movie):
		self.movie = movie
		self.score=0
		self.divider=0

	def calcScore(self):
		if self.divider>0:
			self.score/=self.divider
			self.score = round(self.score,2)

	def get_movie_link(self):
		return("watch/"+str(self.movie.id))

class tickAccess():
	def __init__(self, nr):
		self.nr = nr
		self.access = "avb"
		self.rownr = 0