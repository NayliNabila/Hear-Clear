from django.contrib import admin
from .models import Profile, SongFile, Comments

# Register your models here.
admin.site.register(Profile)
admin.site.register(SongFile)
admin.site.register(Comments)
admin.site.site_url = "/HearClear"