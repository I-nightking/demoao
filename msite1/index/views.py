from django.shortcuts import render
from .models import AndroidFile,AndroidText,AndroidTitle,AndroidSubtitle
from django.http import HttpResponse
# Create your views here.
def index(request):
    title = AndroidTitle.objects.all()
    subtitle = AndroidSubtitle.objects.all()     
    mtext = AndroidText.objects.all()
    mfile = AndroidFile.objects.all()           
    return render(request,'index.html',{"title":title,"subtitle":subtitle,"mtext":mtext,"mfile":mfile})

def content(request):
    return render(request,'content.html')