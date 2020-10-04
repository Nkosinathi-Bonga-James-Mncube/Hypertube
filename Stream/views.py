from django.shortcuts import render
from django.core.files import File
from pathlib import Path
from datetime import timedelta
from Profile.models import Comment
import os
import io
from babelfish import *
from subliminal import *
from django.contrib.auth.decorators import login_required
import bencode
import socket
import hashlib
from django.contrib.auth.models import User
from ezflix import Ezflix
from django.http import HttpResponse
from qbittorrent import Client
from urllib.parse import urlparse
import glob
import pathlib
from django.contrib.auth.models import User
from django.urls import resolve
# from pathlib import Path
import time
from Profile.models import Torrent


# import bencode
def Torrent_details(self,qb,link):
    for torrent in self:
        print("Torrent name:", torrent["name"])
        print("Torrent hash:", torrent["hash"])
        qb.toggle_sequential_download(torrent["hash"])
        value=qb.get_torrent(torrent["hash"])
        torrent_path  = os.path.join('static/folder/', torrent["name"])
        print("The torrent: ", value)
        print("The torrent name" ,torrent["name"])
        print("The torrent path : " , torrent_path)
        print("The torrent: ", value['save_path'])
    try:
        file_location=list(Path(torrent_path).rglob('*.mp4'))[0]
        b=Torrent(Info_code=link,title=file_location)
        if Torrent.objects.filter(Info_code=link).count()< 1:
            b.save()
    except:
        torrent_location=Torrent.objects.filter(Info_code=link)[0]
        file_location = torrent_location.title
        print('file_locaion',file_location)
    return file_location

def post_comment(request):
    if request.method == 'POST':
        new_post = Comment(
            user=request.user,
            post=request.POST['post_value'],
            title=request.POST['title']
        )
        new_post.save()
        print("Add new post")
        return HttpResponse("Updated")



def torrent_view(request):
    qb = Client('http://127.0.0.1:8080/')
    qb.login('admin', 'adminadmin')
    BASE_DIR = Path(__file__).resolve().parent.parent
    d_path  = os.path.join(BASE_DIR, 'static/folder/')
    print("Location : " ,qb.get_default_save_path())
    print("The imdb is : " , request.POST['imdb1'])
    if request.method == 'POST':
        ezflix = Ezflix(query=request.POST['title1'], media_type='movie', quality='720p',limit=1)
        shows = ezflix.search()
        # magnet = 'https://webtorrent.io/torrents/big-buck-bunny.torrent'
        magnet = 'https://webtorrent.io/torrents/cosmos-laundromat.torrent'
        if shows is not None:
            for s in shows:
                if s['imdb']==request.POST['imdb1']:
                    print(s['link'])
                    # torrent_location=Torrent.objects.filter(Info_code=s['title'])[0]
                    # print ("Finally",torrent_location.title)
                    # print(torrent_location)
                    qb.download_from_link(magnet,savepath=d_path)
                    time.sleep(90)
                    torrents = qb.torrents(filter='downloading')
                        # for k in info_hash
                            # k.Info code
                            # print("This is the info")
                    
                    path_torrent=Torrent_details(torrents,qb,s['title'])
                    print('--------------------------------------------------------------------------------------')
        else:
            print("Not found") 
    return HttpResponse(path_torrent)

@login_required(login_url='/')
def stream_view(request,*args,**kwargs):
    print("Current_page",request.get_full_path())
    comment= Comment.objects.order_by('date')
    user1 = User.objects.all()
    context = {"user1":user1,"comment":comment}
    # comment= Comment.objects.all()
    return render(request,"stream.html",context)

def torent_detail(request,torrents,value):
    torrent_info = Torrent(
                        Info_code=torrents,
                        title=value,
                        )
    torrent_info.save()

# BASE_DIR = Path(__file__).resolve().parent.parent
# find_video  = os.path.join(BASE_DIR, 'static/folder/')
# videos = scan_videos(find_video)
# videos = Video.fromname('Harley.Quinn.S02E05.Batmans.Back.Man.2160p.DCU.WEBRip.DDP5.1.x265-NTb')
# subtitles=list_subtitles( video,{Language('eng')},multi=False)
# subtitles = list_subtitles([video], {Language('hun')}, providers=['podnapisi'])
# print(subtitles[0])
# my_region = region.configure('dogpile.cache.memory',replace_existing_backend=True)
# subtitles = list_subtitles([videos],Languages='eng')
# print(subtitles[videos])
# subtitles = download_best_subtitles([video], {Language('eng')}, providers=['podnapisi'])
# print("Found:", video)
# print("Subtitles:", subtitles[video])
# video = Video.fromname('Batman Begins (2005) BRRip x264 MKV by RiddlerA')
# subtitles = list_subtitles([video], {Language('eng')}, providers=['podnapisi'])
# my_region = region.configure('dogpile.cache.memory')
# print("the movie is ", video)
# print(subtitles[video])
