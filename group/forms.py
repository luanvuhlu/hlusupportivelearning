__author__ = 'luanvu'
from django import forms
from document.models import Subject
import logging


# class SearchGroupForm(forms.Form):
#     ss=Subject.objects.filter(deactived=False, public='Y')
#     list_subject=(('', 'Choose subject'), )
#     for s in ss:
#         list_subject=list_subject+((s.subject_code, s.subject_short_name and s.subject_short_name or s.subject_name), ) # Add a tupple to another tupple
#     subject=forms.ChoiceField(choices=list_subject, required=False, label="Subject")
#     class_name=forms.CharField(max_length=10, required=False)
#     start=forms.DateTimeField(required=False)
#     end=forms.DateTimeField(required=False)