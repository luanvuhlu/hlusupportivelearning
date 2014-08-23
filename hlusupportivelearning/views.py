from django.http import HttpResponse
from django.shortcuts import render
from news.models import News
# Create your views here.
def get_new_news_list():
    # news=News.objects_all.filter
    return None
def get_user(request):
    return None

def home(request):
    news=get_new_news_list
    user=get_user(request)
    context={request,
             {"news":news},
    }
    return HttpResponse("HOME")
