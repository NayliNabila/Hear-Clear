"""hearclear2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from page import views
from accounts import views as accounts_views
from page.views import AddCommentView, UserEditView, UploadView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('HearClear', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('HearClear/aboutme', views.aboutme),
    path('signup', accounts_views.signup, name='signup'),
    path('HearClear/comments/reply', views.reply, name='reply'),
    path('HearClear/<int:pk>/delete', views.delete_song, name='delete_song'),
    path('HearClear/<int:pk>/', views.songdetails, name='song-detail'),
    path('HearClear/results/', views.searchbar, name='searchbar'),
    path('HearClear/<int:pk>/comments', AddCommentView.as_view(), name='comments'),
    path('HearClear/edit_profile', UserEditView.as_view(), name='edit_profile'),
    path('HearClear/upload', UploadView.as_view(), name = 'upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
