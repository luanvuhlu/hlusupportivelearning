__author__ = 'luanvu'
import logging
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from models import Group, GroupMember
from document.models import Subject

ITEMS_PER_PAGE=30
log=logging.getLogger(__name__)
class GroupManager:
    def get_group(self, id=None, page=None, student=None, user=None):
        if id:
            return self.__get_group_by_id(id)
        if student:
            return self.__get_list_my_groups(page, student)
        if user:
            return  self.__get_list_own_groups(page, user)
        return self.__get_list_groups(page)
    def __get_group_by_id(self, group_id):
        try:
            group=Group.objects.get(pk=group_id, public='Y', activated=True)
        except Group.DoesNotExist:
            group=None
        if group:
            members=GroupMember.objects.filter(group=group, activated=True)
            return GroupEtt(group, members)
        else:
            return None
    def __get_list_groups(self, page):
        groups=None
        all_groups=Group.objects.filter(public='Y', activated=True).order_by('date_created')
        paginator=Paginator(all_groups, ITEMS_PER_PAGE)
        if not page:
            groups = paginator.page(paginator.num_pages)
        else:
            try:
                groups=paginator.page(page)
            except PageNotAnInteger:
                log.debug("Page number not int !")
            except EmptyPage:
                log.debug("Page not found !")
                groups = paginator.page(paginator.num_pages)
        if not groups:
            return None
        return GroupsList(groups)
    def __get_list_my_groups(self, page, student):
        groups=None
        group_list=[]
        members=GroupMember.objects.filter(student=student, activated=True).order_by('add_time')
        for m in members:
            group=self.__get_group_by_id(m.group.id)
            if group and group.group.public=='Y':
                group_list.append(group)
        paginator=Paginator(group_list, ITEMS_PER_PAGE)
        if not page:
            groups = paginator.page(paginator.num_pages)
        else:
            try:
                groups=paginator.page(page)
            except PageNotAnInteger:
                log.debug("Page number not int !")
            except EmptyPage:
                log.debug("Page not found !")
                groups = paginator.page(paginator.num_pages)
        if not groups:
            return None
        return GroupsList(groups)
    def __get_list_own_groups(self, page, user):
        groups=None
        all_groups=Group.objects.filter(user=user, public='Y', activated=True).order_by('date_created')
        paginator=Paginator(all_groups, ITEMS_PER_PAGE)
        if not page:
            groups = paginator.page(paginator.num_pages)
        else:
            try:
                groups=paginator.page(page)
            except PageNotAnInteger:
                log.debug("Page number not int !")
            except EmptyPage:
                log.debug("Page not found !")
                groups = paginator.page(paginator.num_pages)
        if not groups:
            return None
        return GroupsList(groups)
    def create_group(self, subject_code, theory, seminar, name, date_valid, leader_name, phone, email, user, id=None):
        if id:
            try:
                gr=Group.objects.get(id=id)
            except:
                log.debug("Group isnt exist !")
                return None
        else:
            gr=Group()
        try:
            log.debug("Subject code: "+subject_code)
            subject=Subject.objects.get(activated=True, public='Y', subject_code=subject_code)
        except Subject.DoesNotExist:
            log.debug("Subject isnt exist")
            return None
        gr.subject=subject
        gr.user=user
        gr.class_theory=theory
        gr.class_seminar=seminar
        date_obj=datetime.strptime(date_valid, '%m/%d/%Y')
        gr.date_valid_until=date_obj
        gr.group_leader=leader_name
        gr.phone=phone
        gr.email=email
        gr.group_name=name
        return gr
    def remove_member(self, id):
        try:
            m=GroupMember.objects.get(id=id)
            m.delete()
            return True
        except GroupMember.DoesNotExist:
            log.debug("Member does not exist")
            return False
        except:
            log.debug("Remove member error")
            return False
class GroupEtt:
    def __init__(self, group, members):
        self.group=group
        if group:
            self.id=group.id
        self.members=members
class GroupsList:
    def __init__(self, groups):
        self.groups_pag=groups
        self.groups_list=[]
        gr_mng=GroupManager()
        if groups:
            for group in groups:
                self.groups_list.append(gr_mng.get_group(id=group.id))