from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages



def regist_view(request,*args,**kwargs):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user=form.save(commit=False)
                user.is_active=False 
                user.save()
                request.session['email'] =  user.email
                request.session['user_name'] =  user.username
                return redirect("/email")
            else:
                first_name=form.data['first_name']
                last_name=form.data['last_name']

                if not first_name:
                    messages.info(request,"Please enter firstname")
                if not last_name:
                    messages.info(request,"Please enter last name")
                    form = RegistrationForm(request.POST)
                return render(request,"register.html",{'form':form})
        else:
            form = RegistrationForm()
            context = {'form':form}
            return render(request,"register.html",context)



# Create your views here.
