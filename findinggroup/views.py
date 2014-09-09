from django.http import HttpResponse
from django.shortcuts import render
from hlusupportivelearning.views import get_user, get_new_news_list
from django.template import RequestContext, loader
from entity import GroupManager, Group
# Create your views here.
def home(request):
    user=get_user(request)
    news=get_new_news_list(user)
    page = request.GET.get('page')
    if page:
        groups_list=GroupManager.get_list_group(page)
    else:
        groups_list=GroupManager.get_list_group(1)
    template=loader.get_template("findinggroup/index.html")
    context=RequestContext(request,
        {
            'user':user,
            'news':news,
            'groups_list':groups_list,
        }

    )
    return HttpResponse(template.render(context))