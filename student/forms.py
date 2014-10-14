__author__ = 'luanvu'
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.utils.translation import ugettext_lazy as _
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
        labels = {
            'u_class': _('Class'),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            },
        }
class EditStudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditStudentForm, self).__init__(*args, **kwargs)
        self.fields['birthday'].widget.attrs['class']='datepicker'
        for f_name in self.fields:
            field=self.fields[f_name]
            if f_name=='birthday':
                field.widget.attrs['class']='form-control datepicker'
            # elif f_name=='u_class':
            #     field.widget.attrs['class']='form-control select-control'
            else:
                field.widget.attrs['class']='form-control'
    class Meta:
        model=Student
        fields=['first_name', 'last_name', 'alias', 'email', 'mobile_phone', 'telephone', 'birthday']
        labels = {
            'u_class': _('Class'),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            },
        }
