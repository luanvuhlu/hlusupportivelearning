from django.http import HttpResponse
from django.shortcuts import render
from hlusupportivelearning.views import get_user
from django.template import RequestContext, loader
from forms import StudentForm
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
    return HttpResponse(code)

def create_student_view(request):

    if request.method=='POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            new_student=form.save(commit=False)
            new_student.account=request.user
            new_student.save()
    form=StudentForm()
    return render(request, 'student/create_student.html', {
        'form':form,
    })