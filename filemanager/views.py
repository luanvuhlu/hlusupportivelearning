from django.shortcuts import render
from models import FileStorage, FileType, FileStorageTmp
from django.http import HttpResponse, Http404, HttpResponseRedirect
# Create your views here.
LIMIT_UPLOAD=5
def limited_upload(user):
	try:
		count=FileStorageTmp.objects.filter(uploader=user, current_session=True).count()
		return count > 5
	except:
		return False
def upload_file(request):
    if limited_upload(request.user):
        return HttpResponse("<script>alert('Limited !');</script>")
    file=request.FILES['file']
    return HttpResponse('Error')

