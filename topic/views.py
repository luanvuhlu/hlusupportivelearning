from django.http import HttpResponse
from django.shortcuts import render
from hlusupportivelearning.views import get_user
# Create your views here.
def home(request):
    user=get_user(request)
    return HttpResponse("HOME TOPIC")