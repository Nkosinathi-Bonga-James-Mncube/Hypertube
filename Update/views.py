from django.shortcuts import render,redirect
from Register.forms import RegistrationForm,EditForm,EditUserDetail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def update_view(request,*args,**kwargs):
    if request.method == 'POST':
        form = EditForm(request.POST, instance=request.user)
        form2 = EditUserDetail(request.POST,request.FILES, instance=request.user.user_profile)
        # form2 = EditUserDetail()
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            message="Details are updated"
            context={
                "message":message,
                "form": form
            }
            return render(request,"update.html",context)
    else:
        form = EditForm(instance=request.user)
        form2 = EditUserDetail(instance=request.user)
        context = {
            "form":form,
            "form2":form2
        }
        return render(request,"update.html",context)