from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from hlusupportivelearning.views import get_user
from hlusupportivelearning.util import ErrorMessage
from django.template import RequestContext, loader
from models import Topic, TopicView, TopicGuestView, TopicThanks
from django.utils import timezone
from forms import WriteTopicForm
from filemanager.models import FileStorage, FileType, FileStorageTmp
import hashlib
import logging
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from entity import TopicDetail
ITEMS_PER_PAGE=30
# Create your views here.
log=logging.getLogger(__name__)
def home(request):
    page=request.GET.get('page') and request.GET.get('page') or 1 # if page request does not exist, page=1
    user=get_user(request)
    all_topics=Topic.objects.filter(activated=True, public=True, block=False).order_by('created_time')
    paginator=Paginator(all_topics, ITEMS_PER_PAGE)
    try:
        ls_topics=paginator.page(page)
    except PageNotAnInteger:
        log.debug("Page number not int !")
    except EmptyPage:
        log.debug("Page not found !")
        ls_topics = paginator.page(paginator.num_pages)
    return render(request, 'topic/index.html', {
        'ls_topics':ls_topics,
    })
@login_required(login_url='/account/login/')
def update_view(request, id=None):
    errors=ErrorMessage()
    file_type_list=FileType.objects.filter(activated=True)
    if request.method=='POST':
        form=WriteTopicForm(request.POST)
        # code=request.POST['code']
        if form.is_valid():
            get_object_or_404(Topic, id=id, user=request.user, activated=True, block=False)
            new_topic=form.save(commit=False)
            new_topic.id=id
            new_topic.user=request.user
            if id:
                new_topic.edited=True
            new_topic.save()
            new_topic.tag=form.cleaned_data['tag']
            file_storages=request.POST.getlist('file-storage')
            for f in file_storages:
                try:
                    f_tmp=FileStorageTmp.objects.get(id=f)
                    att=f_tmp.convert()
                    if att:
                        new_topic.attach.add(att)
                    else:
                        return HttpResponse("ERROR")
                except:
                    return HttpResponse('ERROR')
            # new_topic.save()
            return HttpResponseRedirect(reverse('view-topic-detail', args=(new_topic.id, ) ))
        else:
            log.debug(form.errors)
    else:
        code=hashlib.md5(timezone.now().__str__()+"-"+str(request.user.id)).hexdigest()
        if id:
            topic=get_object_or_404(Topic, id=id, user=request.user, activated=True, block=False)
            form=WriteTopicForm(instance=topic)
        else:
            form=WriteTopicForm()
    context={
        'id':id,
        'form':form,
        'code':code,
        'file_type_list':file_type_list,
        'errors':errors,
    }
    if id:
        context['files']=topic.attach.all()
    return render(request, 'topic/save.html', context)
def add_view_count(topic, user):
	if not topic or not isinstance(topic, Topic) :
		log.debug("Topic is not a Topic instance")
		return
	if user:
		nv=TopicView()
		nv.topic=topic
		nv.user=user
		nv.save()
	else:
		ngv=TopicGuestView()
		ngv.topic=topic
		ngv.save()
def view_topic_detail(request, pk):
    user=get_user(request)
    topic_view=get_object_or_404(Topic, id=pk, public=True, block=False)
    topic_detail=TopicDetail(user, topic_view)
    add_view_count(topic_view, user)
    return render(request, 'topic/detail.html', {
        'topic_detail':topic_detail,
    })
