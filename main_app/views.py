from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
import boto3

# constants
S3_BASE_URL = 'https://s3-us-west-2.amazonaws.com/'
BUCKET = '629catcollector'

# Create your views here.
