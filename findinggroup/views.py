from django.http import HttpResponse
from django.shortcuts import render
import logging
from hlusupportivelearning.views import get_user, get_new_news_list
from django.template import RequestContext, loader
from entity import GroupManager, Group
from document.models import Subject
from studentinfo.models import Student
from findinggroup.models import FindingGroupNews, GroupMember, GroupMemberUnknown
from forms import SearchGroupForm

ITEMS_PER_PAGE=30
log=logging.getLogger(__name__)
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
def create_new_view(request):
    user=get_user(request)
    news=get_new_news_list(user)
    if request.method=='POST':
        log.debug('submit form')
        codes=request.POST.getlist('code')
        names=request.POST.getlist('name')
        is_members=request.POST.getlist('is-member')
        subject_code=request.POST.get('subject-code')
        subject_theory=request.POST.get('theory')
        subject_seminar=request.POST.get('seminar')
        group_name=request.POST.get('group-name')
        date_valid=request.POST.get('date-valid')
        leader_name=request.POST.get('leader-name')
        leader_phone=request.POST.get('leader-phone')
        leader_email=request.POST.get('leader-email')
        gr=FindingGroupNews.create_group(subject_code, subject_theory, subject_seminar, date_valid, leader_name, leader_phone, leader_email, request.user)
        log.debug('Subject Code %s', subject_code)
        log.debug('Subject Theory %s', subject_theory)
        log.debug('Subject Seminar %s', subject_seminar)
        log.debug('Group name %s', group_name)
        log.debug('Date valid %s', date_valid)
        log.debug('Name %s', leader_name)
        log.debug('Phone %s', leader_phone)
        log.debug('Email %s', leader_email)
        if not gr:
            return HttpResponse('Gr None')
        gr.save()
        for code, name, is_member in zip(codes, names, is_members):
            if not code or not name or is_member== '-1':
                continue
            if is_member=='0':
                mb=GroupMemberUnknown()
                mb.finding_group=gr
                mb.member_student_code=code
                mb.full_name=name
                mb.save()
                continue
            if is_member=='1':
                try:
                    student=Student.objects.get(deactived=False, student_code=code)
                    mb=GroupMember()
                    mb.finding_group=gr
                    mb.student=student
                    mb.save()
                except Student.DoesNotExist:
                    mb=GroupMemberUnknown()
                    mb.finding_group=gr
                    mb.member_student_code=code
                    mb.full_name=name
                    mb.save()
                    continue
        template=loader.get_template("findinggroup/create-new-success.html")
        context=RequestContext(request,
            {
                'user':user,
                'news':news,
                'gr':gr,
            }
        )
        return HttpResponse(template.render(context))
    all_subjects=Subject.objects.filter(deactived=False, public='Y')
    log.debug(all_subjects)
    template=loader.get_template("findinggroup/create-new.html")
    context=RequestContext(request,
        {
            'user':user,
            'news':news,
            'all_subjects':all_subjects,
        }
    )
    return HttpResponse(template.render(context))
def my_group_view(request):
    return HttpResponse("Create")