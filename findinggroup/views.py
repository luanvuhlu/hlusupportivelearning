from django.http import HttpResponse
from django.shortcuts import render
from hlusupportivelearning.views import get_user
from django.template import RequestContext, loader
# Create your views here.
def home(request):
    user=get_user(request)
    template=loader.get_template("findinggroup/index.html")
    context=RequestContext(request,
        {
            'user':user,
        }

    )
    return HttpResponse(template.render(context))