from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import RequestContext, loader
from django.db.models import Q
import sys
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from news.models import News, NewsView
import logging
NEWS_PER_PAGE=30
log=logging.getLogger(__name__)
# Create your views here.
def get_new_news_list(user=None):
    news=News.objects.filter(public='Y', deactived=False).order_by('created_time')[:10]
    news_list=[]
    for n in news:
        news_list.append(NewsObject(user, n))
    return news_list
class NewsObject:
    def __init__(self, user, news):
        self.id=news.id
        self.title=news.title
        if not user:
            self.seen=False
        else:
            try:
                news_view=NewsView.objects.filter(news=news, user=user)
                if news_view:
                    self.seen=True
            except:
                log.debug("Unexpected error:", sys.exc_info()[0])
def get_user(request):
    if request.user.is_authenticated():
        return request.user
    return None
def home(request):
    log.debug("This is a debug message")
    template=loader.get_template("index.html")
    user=get_user(request)
    news=get_new_news_list(user=user)
    user=get_user(request)
    context=RequestContext(request,
             {
                 "news":news,
                 'user':user,
              }
    )
    return HttpResponse(template.render(context))
def getting_started(request):
    user=get_user(request)
    template=loader.get_template("topic/index.html")
    context=RequestContext(request,
        {           
        }
    )
    return HttpResponse(template.render(context))
def search_full(request):
    template=loader.get_template("search_full.html")
    user=get_user(request)
    news=get_new_news_list(user=user)
    search = request.GET.get('q', '')
    # news_search=News.objects.filter(Q(title__search=search) | Q(header__search=search))
    news_search_list=News.objects.filter(title=search)

    paginator = Paginator(news_search_list, NEWS_PER_PAGE)
    page = request.GET.get('page')
    log.debug(page)
    try:
        news_search = paginator.page(page)
    except PageNotAnInteger:
        log.debug("Page number not int !")
        # If page is not an integer, deliver first page.
        news_search = paginator.page(1)
    except EmptyPage:
        log.debug("Page not found !")
        raise Http404
        # If page is out of range (e.g. 9999), deliver last page of results.
        news_search = paginator.page(paginator.num_pages)

    context=RequestContext(request,
             {
                 "news":news,
                 'news_search':news_search,
                 'user':user,
                 'search':search,
              }
    )
    return HttpResponse(template.render(context))



    