__author__ = 'luanvu'
import json
from dajaxice.decorators import dajaxice_register
from student.models import Student
from entity import GroupManager
@dajaxice_register
def check_exist_student(request, number, code):
    try:
        student=Student.objects.get(activated=True, student_code=code)
    except Student.DoesNotExist:
        return json.dumps({'number':number, 'code':''})
    full_name=student.user.get_full_name()
    return json.dumps({'number':number, 'code':code, 'full_name':full_name})
def remove_member(request, id):
    gr_mng=GroupManager()
    res=gr_mng.remove_member(id)
    return json.dump({'result':res})