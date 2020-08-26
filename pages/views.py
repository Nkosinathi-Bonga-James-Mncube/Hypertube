from django.shortcuts import render
# Create your views here.
def login_view(request,*args,**kwargs):
    return render(request,"login.html")
def home_view(request,*args, **kwargs):
    return render(request,"home.html")
def library_view(request,*args,**kwargs):
    return render(request,"library.html")
def video_view(request,*args,**kwargs):
    return render(request,"video.html")
def update_view(request,*args,**kwargs):
    return render(request,"update.html")

