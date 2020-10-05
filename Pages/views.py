from django.shortcuts import render,redirect
from decouple import config
from django.contrib.auth.models import User
from Profile.models import User_Profile
from .forms import LoginForm
from django.contrib.auth.models import User,auth
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import authenticate, login
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from decouple import config
from rest_framework.authtoken.models import Token
from Profile.models import History
# from .forms import UpdateForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = strip_tags(form.cleaned_data['username'])
            password = strip_tags(form.cleaned_data['password'])
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return render(request,"home.html")
            else:     
                form = LoginForm()
                message = "Username/Password is not valid.Otherwise check email to activate account"
                # UID = config('UID')
                # SECRET = config('SECRET')
                # token = Token.objects.create(
                    # UID,SECRET,site:"https://api.intra.42.fr")
                # print("Token", JSON.stringify(token))
                context={"form":form,"message":message}
                return render(request,"login.html",context)
    else:
        form = LoginForm()
        return render(request,"login.html",{"form":form})

@login_required(login_url='/')       
def home_view(request,*args, **kwargs):
        return render(request,"home.html")

@login_required(login_url='/')       
def logout_view(request):
        auth.logout(request)
        return redirect("/")


@login_required(login_url='/')
def library_view(request,*args,**kwargs):
        history= History.objects.filter(user=request.user)
        context = {
            "history":history,
            'API':config('API_KEY_IMDB'),
            'API_2':config('API_KEY_THEMOVIEDB'),
            }
        return render(request,"library.html",context)

def activation_view(request,user1,token1):
    try:
        decode1= urlsafe_base64_decode(user1)
        found=User.objects.get(pk=decode1)
        token_get= User.objects.get(auth_token=token1)
    except User.DoesNotExist:
        token_get= None
        found = None
    if (found== token_get):
        try:
            user = User.objects.get(username=found)
            user.is_active=True
            user.save()
            print("Match")
            print("Token value" , token_get)
            print("Found value" , found)
            return render(request,"activation.html")
        except User.DoesNotExist:
            message = "Please check activation details are correct or resign up"
            context = {
                'message': message
            }
            print("Token value" , token_get)
            print("Found value" , found)
            return render(request,"login.html",context)
        
# Create your views here.
