from django.contrib import admin
from .models import User_Profile,Comment,History,Torrent

admin.site.register(User_Profile)
admin.site.register(Comment)
admin.site.register(History)
admin.site.register(Torrent)
# Register your models here.
