from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from hlusupportivelearning.views import get_user
from hlusupportivelearning.util import ErrorMessage
from django.template import RequestContext, loader
from forms import WriteTopicForm
import logging
# Create your views here.
log=logging.getLogger(__name__)
def home(request):
    user=get_user(request)
    template=loader.get_template("topic/index.html")
    context=RequestContext(request,
        {
            'user':user,
        }

    )
    return HttpResponse(template.render(context))
def create_view(request):
    errors=ErrorMessage()
    if request.method=='POST':
        form=WriteTopicForm(request.POST)
        if form.is_valid():
            new_topic=form.save(commit=False)
            new_topic.user=request.user
            new_topic.save()
            new_topic.tag=form.cleaned_data['tag']
            new_topic.save()
            return HttpResponseRedirect(reverse('topic-info', args=(new_topic.id, ) ))
        else:
            log.debug(form.errors)
    else:
        form=WriteTopicForm()
    return render(request, 'topic/save.html', {
        'form':form,
        'errors':errors,
    })
def info_view(request, pk):
    return HttpResponse(pk)
