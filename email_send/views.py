from django.shortcuts import render

# Create your views here.
def email_view(request,*args,**kwargs):
    return render(request,"user_email/email.html")

