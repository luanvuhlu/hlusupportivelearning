from django.http import HttpResponse, Http404
from django.shortcuts import render
from hlusupportivelearning.views import get_user
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging
from django.utils import timezone
from news.models import News, NewsView, NewsGuestView
from hlusupportivelearning.views import get_new_news_list
from entity import NewsDetail

ITEMS_PER_PAGE=30
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
    page=request.GET.get('page') and request.GET.get('page') or 1 # if page request does not exist, page=1
    user=get_user(request)
    # news=get_new_news_list(user)
    all_news=News.objects.filter(activated=True, public=True).order_by('created_time')
    paginator=Paginator(all_news, ITEMS_PER_PAGE)
    try:
        news=paginator.page(page)
    except PageNotAnInteger:
        log.debug("Page number not int !")
    except EmptyPage:
        log.debug("Page not found !")
        news = paginator.page(paginator.num_pages)
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
		news_view=News.objects.get(id=pk, public=True)
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


