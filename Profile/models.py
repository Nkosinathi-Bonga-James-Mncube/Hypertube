from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class User_Profile(models.Model):
    LANGUAGE    = (
                ("ENG","English"),
                ("GER","German"),
                ("FRE","French"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    language        = models.CharField(max_length=20,choices=LANGUAGE,default="ENG")
    picture = models.ImageField(default='default_user.png')
    def __str__(self):
            return f'{self.user}'

def create_profile(sender,instance,created, **kwargs):
    if created:
       User_Profile.objects.create(user=instance)
       
post_save.connect(create_profile,sender=User)

def update_profile(sender,instance,created, **kwargs):
    if created == False:
        instance.user_profile.save()

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    post=models.TextField(blank=False,max_length=120)
    title=models.TextField(blank=False,max_length=400)
    date=models.DateTimeField(auto_now_add=True)
      
    def __str__(self):
        return '%s %s' % (self.user, self.date.strftime('%H:%M:%S %d/%m/%Y'))
class Torrent(models.Model):
    Info_code=models.TextField(blank=False,max_length=200)
    title=models.TextField(blank=False,max_length=200)
      
class History(models.Model):
    user        = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    title       = models.TextField(blank=False,max_length=240)
    poster      = models.TextField(blank=False,max_length=240)
    plot        = models.TextField(blank=False,max_length=800)
    year        = models.TextField(blank=False,max_length=4)
    actor       = models.TextField(blank=False,max_length=300)
    director    = models.TextField(blank=False,max_length=300)
    rating      = models.TextField(blank=False,max_length=4)
    imdb = models.TextField(blank=False,max_length=8)
    def __str__(self):
        return f'{self.user}'

# 
#Create your models here.
# 