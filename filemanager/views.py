from django.shortcuts import render
from models import FileStorage, FileType, FileStorageTmp
from django.http import HttpResponse, Http404, HttpResponseRedirect
from filebrowser.base import FileObject
from django.utils import timezone
import os
from hlusupportivelearning.settings import MEDIA_ROOT
import logging
# Create your views here.
LIMIT_UPLOAD=5
log=logging.getLogger(__name__)

def upload_file(request):
    log.debug("Uploading.....")
    code=request.POST['code']
    try:
        count=FileStorageTmp.objects.filter(uploader=request.user, code=code,  current_session=True, complete=False).count()
        print str(count)
    except:
		return HttpResponse("<script>alert('Count Error !');</script>")
    if count > 4:
        return HttpResponse("<script>alert('Limited !');</script>")
    try:
        file_type=FileType.objects.get(name=request.POST['file-type'], activated=True)
    except:
        return HttpResponse("<script>alert('File type %s not found !');</script>" % request.POST['file-type'])
    date=timezone.now()
    f=request.FILES['file']
    dir=(date.year, date.month, date.day, code, count+1)
    path=MEDIA_ROOT+'uploads/files_tmp/'
    path2='uploads/files_tmp/'
    # try:
    for item in dir:
        path=path+'%s/' % item
        path2=path2+'%s/' % item
        if os.path.isdir(path):
                continue
        try:
            os.mkdir(path)
        except:
            return HttpResponse("<script>alert('Save file Error !');</script>")

    with open(path+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    # except:
    #     return HttpResponse("<script>alert('Save file Error !');</script>")
    try:
        fst=FileStorageTmp()
        fst.code=code
        fst.complete=False
        fst.name=request.POST['file-name']
        fst.file=FileObject(path=path2+f.name)
        fst.file_type=file_type
        fst.current_session=True
        fst.uploader=request.user
        fst.save()
    except:
        return HttpResponse("<script>alert('Save object Error !');</script>")
    log.debug("Uploaded")
    return render(request, 'filemanager/uploaded-topic-attach-ajax.html', {'file':fst.file, 'file_storage':fst})

