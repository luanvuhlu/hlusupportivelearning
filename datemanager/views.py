from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render
from hlusupportivelearning.views import get_user
from django.template import RequestContext, loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging
from django.utils import timezone
from entity import WorkoutCalendar
from django.shortcuts import render_to_response
from django.utils.safestring import mark_safe
from models import Holiday

ITEMS_PER_PAGE=30
log=logging.getLogger(__name__)
# Create your views here.
def holiday_view(request, year, month):
    year=int(year)
    month=int(month)
    if month < 1 or month > 12 or year < 1:
        raise Http404
    my_workouts = Holiday.objects.order_by('created_time').filter(date__year=year, date__month=month)
    cal = WorkoutCalendar(my_workouts).formatmonth(year, month)
    return render_to_response('datemanager/holiday.html', {'calendar': mark_safe(cal),})