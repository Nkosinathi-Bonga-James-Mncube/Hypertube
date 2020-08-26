from django.db import models

# Create your models here.

class Input_data(models.Model):
    ENGLISH     = 'ENG'
    GERMAN      = 'DEK'
    FRENCH      = 'FRE'
    LANGUAGE    = [
                (ENGLISH,'English'),
                (GERMAN,'German'),
                (FRENCH,'French'),
           ]
    first_name  = models.CharField(blank=False,max_length=120)
    last_name   = models.CharField(blank=False,max_length=120)
    password = models.CharField(blank=False,max_length=20)
    user_name   = models.CharField(blank=False,max_length=2,error_messages={"max_length":"This is too long"})
    email       = models.EmailField(blank=False,max_length=120)
    language = models.CharField(max_length=3,choices=LANGUAGE,default=ENGLISH,)
    
    
    
    
    
    
    
    
    




