__author__ = 'luanvu'
from django import forms
from document.models import Subject
from student.models import Student
import logging
log=logging.getLogger(__name__)

class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['birthday'].widget.attrs['class']='datepicker'
        for f_name in self.fields:
            field=self.fields[f_name]
            if f_name=='birthday':
                field.widget.attrs['class']='form-control datepicker'
            else:
                field.widget.attrs['class']='form-control'
        # for field in self.fields:
        #     field.widget.attrs['class']='form-control'
    class Meta:
        model=Student
        fields=['u_class', 'code', 'first_name', 'last_name', 'alias', 'email', 'mobile_phone', 'telephone', 'birthday']
