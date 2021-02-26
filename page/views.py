from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage

from .form import SongForm, CommentForm
from .models import SongFile, Comments
from django.db import models
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.forms import UserChangeForm

# Create your views here.
def home (request):
    songs = SongFile.objects.all()
    return render(request, 'home.html', {
        'songs' : songs
    })

def songdetails (request, pk):                                                      # function of specific song which will be display in song details page
    songfile = get_object_or_404(SongFile, pk=pk)
    return render (request, 'songfile-detail.html', { 'songfile' : songfile})

def delete_song(request, pk):                                                       # for deleting part
    if request.method == 'POST':
        songs = SongFile.objects.get(pk=pk)
        songs.delete()
        return redirect ('home')

def searchbar(request):                                                             # for searching process
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

class UploadView(CreateView):                                                       # to crate view of the form for uploading the audio
    model = SongFile
    form_class = SongForm
    template_name = 'upload.html'
    #fields = '__all__' 

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id                              # to get user id to record which user is upload the audio
        return super().form_valid(form)
    success_url= reverse_lazy('home')

class AddCommentView(CreateView):                                                   # to create view of the form for comments the song
    model = Comments
    form_class = CommentForm
    template_name = 'comments.html'
    #fields = '__all__' 

    def form_valid(self, form):
        form.instance.songfile_id = self.kwargs['pk']                               # to get the audio id to know which song the user commenting
        return super().form_valid(form)
    success_url= reverse_lazy('home')

class UserEditView(generic.UpdateView):                                             # for edit the profile of user registered
    form_class = UserChangeForm 
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy ('home')

    def get_object(self):
        return self.request.user

