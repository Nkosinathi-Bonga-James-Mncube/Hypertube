from django.shortcuts import render
from .models import History
from django.contrib.auth.models import User
from django.http import HttpResponse

def history(request):
    if request.method == 'POST':
        record = History(title=request.POST['title1'],
        user=request.user,
        poster=request.POST['poster1'],
        imdb=request.POST['imdb1'],
        plot=request.POST['plot1'],
        year=request.POST['year1'],
        actor=request.POST['actors1'],
        director=request.POST['director1'],
        rating=request.POST['rating1'],
        )
        if History.objects.filter(imdb=request.POST['imdb1']).filter(user=request.user).count() < 1:
            record.save()
            print("Movie added: " ,request.POST['title1'])
            print("User name: " ,request.user)
        else:
            print("Already present")         
    return HttpResponse("Complete History added")

def history_view(request):
    history_log = History.objects.filter(user=request.user)
    context={
        "history_log":history_log
    }
    return render(request,"history.html",context)
    
# Create your views here.
