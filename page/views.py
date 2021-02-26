from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
#from django.http import Http404

from .form import SongForm, CommentForm
from .models import SongFile, Comments
from django.db import models
#from .models import ModelWithFileField
#from .songinfo import SongInfo
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.forms import UserChangeForm

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



def reply(request):
    return render(request, 'reply.html')

"""def upload (request):
    if request.method =='POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SongForm()
        return render(request, 'upload.html', {
        'form' : form
    })"""

class UploadView(CreateView):
    model = SongFile
    form_class = SongForm
    template_name = 'upload.html'
    #fields = '__all__' 

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        return super().form_valid(form)
    success_url= reverse_lazy('home')

class AddCommentView(CreateView):
    model = Comments
    form_class = CommentForm
    template_name = 'comments.html'
    #fields = '__all__' 

    def form_valid(self, form):
        form.instance.songfile_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url= reverse_lazy('home')

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm 
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy ('home')

    def get_object(self):
        return self.request.user



#def comments (request):
 #   if request.method =='POST':
  #      form = CommentsForm(request.POST, request.FILES)
   #     if form.is_valid():
    #        form.save()
     #       return redirect('song-detail')
      #      
    #else:
     #   form = CommentsForm()
      #  return render(request, 'comments.html', {
       # 'form' : form})



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