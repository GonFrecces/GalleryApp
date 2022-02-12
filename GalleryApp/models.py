from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
# 40mb es lo que soporta django .

class GalleryImage(models.Model):
    Name= models.CharField(max_length=100)
    Image= models.FileField(upload_to='media/Images/%y',null=True, blank=True,verbose_name="Images")

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.Image.path):
            os.remove(self.Image.path)
        super(GalleryImage, self).delete(*args, **kwargs)
        
    def __str__(self):
        return '%s,%s' %(self.Name,self.Image)


class GalleryVideo(models.Model):
    Name= models.CharField(max_length=100)
    Video= models.FileField(upload_to='media/Videos/%y',null=True, blank=True,verbose_name="Videos")

    def delete(self, *args, **kwargs):
        if os.path.isfile(self.Video.path):
            os.remove(self.Video.path)
        super(GalleryVideo, self).delete(*args, **kwargs)
        
    def __str__(self):
        return '%s,%s' %(self.Name,self.Video)