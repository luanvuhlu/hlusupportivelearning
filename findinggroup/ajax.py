__author__ = 'luanvu'
import json
from dajaxice.decorators import dajaxice_register
from studentinfo.models import Student

@dajaxice_register
def check_exist_student(request, number, code):
    try:
        student=Student.objects.get(deactived=False, student_code=code)
    except Student.DoesNotExist:
        return json.dumps({'number':number, 'code':''})
    full_name=student.user.get_full_name()
    return json.dumps({'number':number, 'code':code, 'full_name':full_name})
