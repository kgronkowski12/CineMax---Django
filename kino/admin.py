from django.contrib import admin
from .models import *

admin.site.register(Movie)
admin.site.register(Repertoire)
admin.site.register(Comment)
admin.site.register(Ticket)
admin.site.register(Genre)
admin.site.register(Director)