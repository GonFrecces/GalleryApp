from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from django import forms
from .models import User, GalleryImage,GalleryVideo


class CustomUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs,):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'type':'text',
            'class':'form-control',
            'name':'username',
            'id':'floatingInput',
            'placeholder':'Username'})
        self.fields['password2'].widget.attrs.update({
            'type':'text',
            'class':'form-control',
            'name':'username',
            'id':'floatingInput',
            'placeholder':'Username'})

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
         'username':forms.TextInput(attrs={'type':'text','class':'form-control','name':'username','id':'floatingInput','placeholder':'Username','margin-bottom': '10px;'}),
         'email':forms.EmailInput(attrs={'type':'email','class':'form-control','name':'email','id':'floatingInput','placeholder':'Email'}),
         'password1':forms.PasswordInput(attrs={'type':'password','class':'form-control','name':'password1','id':'floatingInput','placeholder':'Password1'}),
         'password2':forms.PasswordInput(attrs={'type':'password','class':'form-control','name':'password2','id':'floatingInput','placeholder':'Password2'}),
      }




class ImageForm(forms.ModelForm):
    class Meta:
        model= GalleryImage
        fields= '__all__'

class VideoForm(forms.ModelForm):
    class Meta:
        model= GalleryVideo
        fields= '__all__'