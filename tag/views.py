from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from hlusupportivelearning.views import get_user
from django.template import RequestContext, loader
from student.models import Student
from models import Tag
from entity import StudentTag
from hlusupportivelearning.util import ErrorMessage
import logging
log=logging.getLogger(__name__)

# Create your views here.
def student_tag_view(request, code):

    errors=ErrorMessage()
    template='tag/student.html'
    if request.method=='POST':
        tags=request.POST.getlist('tag')
        student=get_object_or_404(Student, account=request.user, code=code, activated=True, block=False)
        tags_of_student=student.tags.all()
        new_tags_of_student=[]
        for tag_id in tags:
            if not tag_id:
                continue
            tag=get_object_or_404(Tag, id=tag_id, is_public=True, activated=True)
            new_tags_of_student.append(tag)
            if tag not in tags_of_student:
                student.tags.add(tag)
        for tag in tags_of_student:
            if tag.id not in tags:
                student.tags.remove(tag)
        student.save()
        all_tags=Tag.objects.filter(activated=True, is_public=True)
        # tags_of_student=student.tags.all()
        tags=[]
        for tag in all_tags:
            tags.append(StudentTag(tag, (tag in new_tags_of_student)))
        return render(request, template, {
        'errors':errors,
        'student':student,
        'tags':tags,
        })
    student=get_object_or_404(Student, account=request.user, code=code, activated=True, block=False)
    student_tags=student.tags.all()
    # log.debug(student_tags)
    tags=[]
    all_tags=Tag.objects.filter(activated=True, is_public=True)
    for tag in all_tags:
        tags.append(StudentTag(tag, (tag in student_tags)))
    return render(request, template, {
        'errors':errors,
        'student':student,
        'tags':tags,
    })
