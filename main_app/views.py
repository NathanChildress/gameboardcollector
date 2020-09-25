from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3
from .models import Boardgame, Genre, Reviews

# constants
S3_BASE_URL = 'https://s3-us-west-2.amazonaws.com/'
BUCKET = '629catcollector'

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def games_index(request):
    games = Boardgame.objects.filter(user=request.user)
    return render(request, 'boardgames/index.html', {'boardgames': games})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class BoardGameCreate(LoginRequiredMixin, CreateView):
  model = Boardgame
  fields = ['name', 'genre', 'desc']

  def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)


class BoardGameUpdate(LoginRequiredMixin, UpdateView):
  model = Boardgame
  fields = ['genre', 'desc']

class ReviewDelete(LoginRequiredMixin, DeleteView):
  model = Review
  success_url = '/boardgames/'