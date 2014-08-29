from django.http import HttpResponse
from django.shortcuts import render
from hlusupportivelearning.views import get_user
import logging

log=logging.getLogger(__name__)
# Create your views here.
def home(request):
    log.debug("This is a debug message")
    user=get_user(request)
    return HttpResponse("HOME ACCOUNT")