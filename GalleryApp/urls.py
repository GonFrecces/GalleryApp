
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('example/', views.example, name='example'),
    path('example2/', views.example2, name='example2'),
    path('gallery/', views.ImageGallery, name='gallery'),
    path('video/', views.VideoGallery, name='video'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
