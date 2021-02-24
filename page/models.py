from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.core.files.images import ImageFile

import librosa 
import librosa.display
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# Create your models here.

class HearClear(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Type(models.Model):
    type = models.CharField(max_length = 10)

    def __str__(self):
        return self.type

class SongFile(models.Model):
    title = models.CharField(max_length = 100)
    audio = models.FileField(upload_to= 'songs')
    image = models.ImageField(upload_to='audioimage/image')
    date = models.DateTimeField(default=timezone.now)
    duration = models.CharField(max_length=10)
    samp_freq = models.DecimalField(null=True,max_digits=10,decimal_places=2)
    file_size = models.FloatField(null=True, blank=True, default=None)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('songfile-detail', kwargs={'pk': self.pk})

    def save (self, *args, **kwargs):
        super(SongFile,self).save(*args, **kwargs)
        dir_image = "./media/audioimage/image"
        imagePath = dir_image + str(timezone.now()) + ".png"
        audio, sr = librosa.load(self.audio.path)
        fig, ax = plt.subplots(1)
        ax.set(title='Waveform')
        ax.label_outer()
        librosa.display.waveplot(audio, sr=sr, ax=ax)
        plt.show()
        plt.savefig(imagePath)
        self.image = ImageFile(open(imagePath, 'rb'))
        self.duration = librosa.get_duration(y=audio,sr=sr)
        file_size_byte = os.path.getsize(self.audio.path)
        self.file_size = file_size_byte/1024
        self.samp_freq = sr
        super(SongFile,self).save(*args, **kwargs)

        def delete(self, *args, **kwargs):
            self.title.delete()
            self.audio.delete()
            self.image.delete()
            super().delete(*args, **kwargs)
