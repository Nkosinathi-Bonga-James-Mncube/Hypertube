from django.shortcuts import render
from django.contrib.auth.models import User
from Profile.models import History
from django.contrib.auth.decorators import login_required

@login_required(login_url='/') 
def search_view(request):
    all_user = User.objects.all()
    if request.method == 'POST':
        print("Got request: ",request.POST.get("search_element"))
        found = User.objects.filter(username=request.POST.get("search_element"))
        try:
            user1 = User.objects.get(username=request.POST.get("search_element"))
            history_search = History.objects.filter(user=user1)
        except:
            history_search = None
        context = {
            "all_user":all_user,
            "found": found,
            "history_search": history_search
        }
        return render(request,"search.html",context)
    else:
        return render(request,"search.html",{"all_user":all_user})
# Create your views here.
