from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from hlusupportivelearning.views import get_user
from django.template import RequestContext, loader
from student.models import Student
from forms import StudentForm, EditStudentForm
from hlusupportivelearning.util import ErrorMessage
import logging
log=logging.getLogger(__name__)
# Create your views here.
def home(request):
    user=get_user(request)
    template=loader.get_template("student/index.html")
    context=RequestContext(request,
        {
            'user':user,
        }

    )
    return HttpResponse(template.render(context))
def info_view(request, code):
    student=get_object_or_404(Student, code=code)
    return render(request, 'student/info.html', {'student':student, })
    return HttpResponse(code)
def my_student(request):
    errors=ErrorMessage()
    try:
        student=Student.objects.get(account=request.user)
    except:
        errors.add_err("You don't have a student account !")
        return render(request, 'student/info.html', {'errors':errors, })
    return HttpResponseRedirect(reverse('student-info', args=(student.code, ) ))
def create_view(request):
    errors=ErrorMessage()
    try:
        student=Student.objects.get(account=request.user, block=False, activated=True)
        errors.add("ExistStudent")
        return render(request, 'student/save.html', {'errors':errors, 'student':student, })
    except:
        log.debug("Cannot find student")
    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            new_student=form.save(commit=False)
            new_student.account=request.user
            new_student.save()
            return HttpResponseRedirect(reverse('student-info', args=(new_student.code, ) ))
        else:
            log.debug(form.errors)
    else:
        form=StudentForm()
    return render(request, 'student/save.html', {
        'form':form,
    })
def edit_view(request, code):
    errors=ErrorMessage()
    try:
        student=get_object_or_404(Student, account=request.user, code=code, block=False, activated=True)
    except:
        errors.add_err('Stundet does not exist')
        log.debug("Cannot find student")
    if request.method=='POST':
        form=EditStudentForm(request.POST, instance=student)
        if form.is_valid():
            new_student=form.save(commit=False)
            new_student.account=request.user
            new_student.save()
            return HttpResponseRedirect(reverse('student-info', args=(new_student.code, ) ))
        else:
            log.debug(form.errors)
    else:
        form=EditStudentForm(instance=student)
    return render(request, 'student/save.html', {
        'form':form,
        'student':student,
    })