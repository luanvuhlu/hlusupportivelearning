from django.http import HttpResponse, Http404
from django.shortcuts import render
from hlusupportivelearning.views import get_user
from django.template import RequestContext, loader
from datetime import datetime
import logging
from django.utils import timezone
from news.models import News, NewsView, NewsGuestView
from hlusupportivelearning.views import get_new_news_list
from entity import NewsDetail

log=logging.getLogger(__name__)
# Create your views here.
def add_view_count(news, user):
	if not news or not isinstance(news, News) :
		log.debug("News is not a News instance")
		return
	if user:
		nv=NewsView()
		nv.news=news
		nv.view_time=timezone.now()
		nv.user=user
		nv.save()
	else:
		ngv=NewsGuestView()
		ngv.news=news
		ngv.view_time=timezone.now()
		ngv.save()
def home(request):
    user=get_user(request)
    news=get_new_news_list(user)
    template=loader.get_template("news/index.html")
    context=RequestContext(request,
        {
            'user':user,
            'news':news,
        }
    )
    return HttpResponse(template.render(context))
def view_news_detail(request, pk):
	user=get_user(request)
	news=get_new_news_list(user=user)
	try:
		news_view=News.objects.get(id=pk, public='Y')
		news_detail=NewsDetail(user, news_view)
		add_view_count(news_view, user)
	except News.DoesNotExist:
		raise Http404
	template=loader.get_template("news/news_detail.html")
	context=RequestContext(request, { 
			'user':user, 
			'news':news,
			'news_detail':news_detail,
	})
	return HttpResponse(template.render(context))


