from django.shortcuts import render,redirect
from api.models import blog
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
@login_required(login_url='/login')
def home(request):
    blogs =blog.objects.all()
    return render(request,"tech-category-01.html",{'blogs':blogs})
def my_post(request):
    blogs=blog.objects.filter(author=request.user)
    return render(request,'tech-author.html',{'blogs':blogs})
@login_required(login_url='/login')
def add_blog(request):
    if request.method=="POST":
        title=request.POST['title']
        image=request.FILES.get('image')
        content=request.POST['content']
        new=blog.objects.create(author=request.user,title=title,image=image,content=content)
        new.save()
        return redirect("/")
    return render(request,"post-blog.html")
def login_view(request):
    username =request.POST.get('uname')
    password=request.POST.get('psw')
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('/')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('/login') 
