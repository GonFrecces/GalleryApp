from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, logout
from django.contrib import messages
from GalleryApp.forms import CustomUserForm , ImageForm,VideoForm
from .models import GalleryImage,GalleryVideo
# Create your views here.
def index(request):
    return render(request, "Aplicacion/home.html")


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user)
            return redirect(to='gallery')
        else:
            messages.warning(
                request, "El usuario o contraseña no coinciden, intentelo denuevo.")
            return redirect(to='login')

    else:
        return render(request, 'Aplicacion/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def register(request):
    forms = CustomUserForm()
    if request.method == 'POST':
        forms = CustomUserForm(request.POST)
        try:
            if forms.is_valid():
                forms.save()
                messages.success(
                    request, "Ahora que ya estas registrado... ingresa con tus credenciales")
                return redirect('login')
        except Exception as e:
            messages.warning(request, "El usuario no se ha podido Registrar"+e)
            return redirect('register')
    else:
        context = {'forms': forms}
        return render(request, "Aplicacion/register.html", context)



def example(request):
    return render(request, 'Aplicacion/example.html')


def example2(request):
    return render(request, 'Aplicacion/example2.html')




def ImageGallery(request):
    imagefile = GalleryImage.objects.all()
    form = ImageForm()
    context = {'form':form, 'image':imagefile}
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Imagen guardado con exito.") 
            return redirect('gallery')
    return render(request, 'Aplicacion/Gallery.html',context)



def VideoGallery(request):
    videofile = GalleryVideo.objects.all() 
    form = VideoForm()
    context = {'form':form, 'video': videofile}
    if request.method == 'POST':
        check_ = request.POST.getlist('checks[]')
        for i in check_:
            b = GalleryVideo.objects.get(id=i)
            print(b)
            b.delete()
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Video guardado con exito.") 
            return redirect('video')
    else:
         context = {'form':form, 'video': videofile}    
    return render(request, 'Aplicacion/video.html', context)






def ImageGallery_delete(request):
    if request.method == 'POST':
        check_ = request.POST.getlist('checks[]')
        for i in check_:
            b = GalleryImage.objects.get(id=i)
            b.delete()
            messages.success(request, "Imagen eliminado con exito.") 
        
    return redirect('gallery')