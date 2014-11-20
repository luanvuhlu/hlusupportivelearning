__author__ = 'luanvu'
from django import forms
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from django.utils.translation import ugettext_lazy as _
from ckeditor.widgets import CKEditorWidget
from django_select2.widgets import Select2MultipleWidget
from django.forms.widgets import Textarea, TextInput
from models import Topic

from document.models import Subject
from student.models import Student
import logging
log=logging.getLogger(__name__)

class WriteTopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['title', 'header', 'content', 'tag']
        widgets = {
            'tag': Select2MultipleWidget(select2_options={
                                'placeholder':'Type and Choice Tags',
                                'minimumResultsForSearch': 10,
                                'closeOnSelect': False,
                                }),
        }
