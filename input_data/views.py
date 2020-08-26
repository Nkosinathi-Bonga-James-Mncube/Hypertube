from django.shortcuts import render
from .forms import InputDataForm
from .models import Input_data
from django.contrib.auth.hashers import make_password,check_password
from django.utils.html import strip_tags
from django.core.mail import send_mail

def regist_view(request):
    form = InputDataForm()
    hold= {}
    if request.method == 'POST':
        form = InputDataForm(request.POST)
        if form.is_valid():
            hold={ 'first_name' :strip_tags(form.cleaned_data['first_name']) , 
                  'last_name' : strip_tags(form.cleaned_data['last_name']),   
                  'user_name': strip_tags(form.cleaned_data['user_name']),   
                  'password': strip_tags(make_password(form.cleaned_data['password'])),    
                  'email' : strip_tags(form.cleaned_data['email'])  }    
            Input_data.objects.create(**hold)
            # print(check_password('1234','pbkdf2_sha256$216000$mOepe7A5vHoI$a+w8CG9v9w8l5bLsspXpYpdnquQQIikWZvYmgkz17XA='))
            
        # else:
            # print(form.errors()
    context = {
        'form': form,
        'try':hold}

    return render(request,"user_input/register.html",context)
# Create your views here.
