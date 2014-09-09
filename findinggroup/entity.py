__author__ = 'luanvu'
import logging
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import FindingGroupNews, GroupMember, GroupMemberUnknown

ITEMS_PER_PAGE=30
log=logging.getLogger(__name__)
class GroupManager:
    @staticmethod
    def get_group_by_id(group_id):
        try:
            group=FindingGroupNews.objects.get(pk=group_id, public='Y', deactived=False)
        except FindingGroupNews.DoesNotExist:
            group=None
        if group:
            members=GroupMember.objects.filter(finding_group=group, deactived=False)
            unknown_members=GroupMemberUnknown.objects.filter(finding_group=group)
            return Group(group, members, unknown_members)
        else:
            return None
    @staticmethod
    def get_list_group(page):
        groups=None
        all_groups=FindingGroupNews.objects.filter(public='Y', deactived=False).order_by('date_created')
        paginator=Paginator(all_groups, ITEMS_PER_PAGE)
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
class Group:
    def __init__(self, group, members, unknown_members):
        self.group=group
        self.members=members
        self.unknown_members=unknown_members
class GroupsList:
    def __init__(self, groups):
        self.groups_pag=groups
        self.groups_list=[]
        if groups:
            for group in groups:
                self.groups_list.append(GroupManager.get_group_by_id(group.id))