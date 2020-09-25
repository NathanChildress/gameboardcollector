from django.contrib import admin
from .models import Boardgame, Reviews, Genre

# Register your models here.
admin.site.register(Genre)
admin.site.register(Boardgame)
admin.site.register(Reviews)