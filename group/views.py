from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
import logging
from hlusupportivelearning.views import get_user, get_new_news_list
from django.template import RequestContext, loader
from entity import GroupManager, Group
from document.models import Subject
from student.models import Student
from group.models import Group, GroupMember
from django.utils import timezone
# from forms import SearchGroupForm

ITEMS_PER_PAGE=30
log=logging.getLogger(__name__)
# Create your views here.
def home(request):
    user=get_user(request)
    news=get_new_news_list(user)
    page = request.GET.get('page')
    gr_mng=GroupManager()
    if request.GET.get('mgr')=='1':
        student=Student.objects.filter(user=user)
        if student:
            title="Your group is member"
            groups_list=gr_mng.get_group(page=page, student=student)
        else:
            groups_list=None
    elif request.GET.get('mgr')=='0':
        title="Your group"
        groups_list=gr_mng.get_group(page=page, user=user)
    else:
        title='Groups'
        groups_list=gr_mng.get_group(page=page)
    template=loader.get_template("group/index.html")
    context=RequestContext(request,
        {
            'title':title,
            'user':user,
            'news':news,
            'groups_list':groups_list,
        }
    )
    return HttpResponse(template.render(context))
def save_group_view(request, id=None):
    user=get_user(request)
    news=get_new_news_list(user)
    is_new=True
    gr_mng=GroupManager()
    try:
        all_subjects=Subject.objects.filter(activated=True, public='Y')
    except Subject.DoesNotExit:
        log.debug("Subject does not exist")
        raise Http404
    if id:
        is_new=False
    if request.method=='POST':
        subject_code=request.POST.get('subject-code')
        subject_theory=request.POST.get('theory')
        subject_seminar=request.POST.get('seminar')
        group_name=request.POST.get('group-name')
        date_valid=request.POST.get('date-valid')
        leader_name=request.POST.get('leader-name')
        leader_phone=request.POST.get('leader-phone')
        leader_email=request.POST.get('leader-email')

        codes=request.POST.getlist('code')
        names=request.POST.getlist('name')
        founds=request.POST.getlist('found')
        member_ids=request.POST.getlist('member-id')

        action=request.POST.get('action')
        if action=='SAVE':
            if is_new:
                gr=gr_mng.create_group(subject_code, subject_theory, subject_seminar, group_name, date_valid, leader_name, leader_phone, leader_email, user)
            else:
                gr=gr_mng.create_group(subject_code, subject_theory, subject_seminar, group_name, date_valid, leader_name, leader_phone, leader_email, user, id=id)
            if not gr:
                raise Http404
            gr.save()

            for code, name, found, id in zip(codes, names, founds, member_ids):
                if not code or not name:
                    continue
                if not id:
                    try:
                        mb=GroupMember.objects.get(id=id)
                    except GroupMember.DoesNotExist:
                        log.debug("Member doest not exist %s", id)
                        raise Http404
                else:
                    mb=GroupMember()
                    mb.group=gr
                mb.student_code=code
                mb.full_name=name
                if not found and found.upper()=='Y':
                    try:
                        student=Student.objects.get(student_code=code)
                    except Student.DoestNotExist:
                        log.debug("Student doest not exist %s", code)
                        raise Http404
                    mb.found_yn=True
                    mb.member_code=code
                mb.save()
            template=loader.get_template("group/create-result.html")
            context=RequestContext(request,
                {
                    'user':user,
                    'news':news,
                    'gr':gr,
                }
            )
        else:
            pass
    else:
        template=loader.get_template("group/create-new.html")
        if not is_new:
            gr=gr_mng.get_group(id=id)
            if not gr:
                raise Http404
        else:
            gr=None
        context=RequestContext(request,
            {
                'user':user,
                'news':news,
                'all_subjects':all_subjects,
                'gr':gr,
            }
        )
    return HttpResponse(template.render(context))
def my_group_view(request):
    return HttpResponse("Create")
class GroupRequestObject:
    def __init__(self):
        pass