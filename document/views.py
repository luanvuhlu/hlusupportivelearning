from django.http import HttpResponse
from django.shortcuts import render
from hlusupportivelearning.views import get_user, get_new_news_list
from django.template import RequestContext, loader
# Create your views here.

def info_view(request, code):
    return HttpResponse(code)