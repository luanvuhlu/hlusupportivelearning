from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader
from news.models import News
import logging

log=logging.getLogger(__name__)
# Create your views here.
def get_new_news_list():
    # news=News.objects_all.filter
    return None
def get_user(request):
    return None

def home(request):
    log.debug("This is a debug message")
    template=loader.get_template("index.html")
    news=get_new_news_list
    user=get_user(request)
    context=RequestContext(request,
             {
                 "news":news,
                 'user':user,
              }
    )

    return HttpResponse(template.render(context))
