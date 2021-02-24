from django.http import HttpResponse
from .models import HearClear
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
#from django.http import Http404

from .form import SongForm
from .models import SongFile
from django.db import models
#from .models import ModelWithFileField
#from .songinfo import SongInfo
from django.views.generic import DetailView

# Create your views here.
def home (request):
    songs = SongFile.objects.all()
    return render(request, 'home.html', {
        'songs' : songs
    })

def songdetails (request, pk):
    songfile = get_object_or_404(SongFile, pk=pk)
    return render (request, 'songfile-detail.html', { 'songfile' : songfile})

def delete_song(request, pk):
    if request.method == 'POST':
        songs = SongFile.objects.get(pk=pk)
        songs.delete()
        return redirect ('home')

def searchbar(request):
    if request.method == "GET":
        search = request.GET.get('search')
        post = SongFile.objects.all().filter(title=search)
        return render (request, 'searchbar.html', {'post' : post})

def aboutme (request):
    return render(request, 'aboutme.html')

def base(request):
    return render(request, 'base.html')

def comments(request):
    return render(request, 'comments.html')

def reply(request):
    return render(request, 'reply.html')

def upload (request):
    if request.method =='POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SongForm()
        return render(request, 'upload.html', {
        'form' : form
    })

#def songs (request):
#    return render(request, 'songs.html')

#class PostSongs():
#    model = Post
#    fields = ['title','content','audio']



"""    def form_valid(self, form):
        form.instance.author =self.request.user
        
        SoundResult =  Sound(form.instance.audio)
        form.instance.image = SoundResult[0]
        form.instance.duration = SoundResult[1]
        form.instance.samp_freq = SoundResult[2]
        
        return super().form_valid(form)"""