from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from rest_framework.authtoken.models import Token
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode


# class TokenCreate(self,user,timestamp):
    # def hash_value():
        # return(text_type(user.pk)+text_type(timestamp))
        # user = request.user
        #  t1 = datetime.datetime.now()
            # t2 = t1.strftime(("%f"))

def email_view(request,*args,**kwargs):
    # if (request.user.is_authenticated == False):
        # return render(request,"login.html")
    # else:
        # user = super(RegistrationForm,self).save(commit=False)
        user_hold = User.objects.get(username=request.session.get("user_name"))
        token = Token.objects.create(user=user_hold)
        user_id = urlsafe_base64_encode(force_bytes((user_hold.pk)))
        title =  'Thank you for registering with Hypertube'
        link = "yoyo"
        link = 'http://'+request.get_host()+'/activation'+'/'+user_id+'/'+token.key+'/'
        subject = 'Hi '+request.session.get("user_name")+', Please click the link to verify your account : <a href="'+link+'">Register to Hypertube</a>'
        # user_hold = User.objects.get(username="nathi").values('email')
        # user1 =UserCreationForm()
        # print("Current page: ",request.user.email)
        #print("Session user :" , request.session.get("user_name"))
        #print("Token generator", token.key)
        #print("User_ID" , urlsafe_base64_encode(force_bytes((user_hold.pk))))
        # print("User ID", User.pk)
        # print('Is user valid: ' , request.user.is_authenticated)
        email=send_mail(
        title,
        subject,
        'from@example.com',
        [request.session.get("email")],
        fail_silently=False) 
        return render(request,"email.html")

# Create your views here.
