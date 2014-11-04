from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from hlusupportivelearning.views import get_user
from hlusupportivelearning.util import ErrorMessage
from django.template import RequestContext, loader
from django.utils import timezone
from forms import WriteTopicForm
from filemanager.models import FileStorage, FileType, FileStorageTmp
import hashlib
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
    file_type_list=FileType.objects.filter(activated=True)
    if request.method=='POST':
        form=WriteTopicForm(request.POST)
        code=request.POST['code']
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
        code=hashlib.md5(timezone.now().__str__()+"-"+str(request.user.id)).hexdigest()
        form=WriteTopicForm()
    return render(request, 'topic/save.html', {
        'form':form,
        'code':code,
        'file_type_list':file_type_list,
        'errors':errors,
    })
def info_view(request, pk):
    return HttpResponse(pk)
