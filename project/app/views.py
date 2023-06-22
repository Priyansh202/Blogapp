from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from .models import *

from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from project import  settings
from django.contrib.auth.decorators import login_required
from .helpers import send_forget_password_mail
import uuid
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm












def home(request):
    return render(request,"app/index.html")
def signup(request):
    
    if request.method =="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist")
            return redirect('home')

        if User.objects.filter(email=email):

            messages.error(request,"email already exist")
            return redirect('home')
        if len(username)>10:
            messages.error(request,"Username must be less than 10 characters")
        if pass1 != pass2:
            messages.error('Password did not match')
        if not username.isalnum():
            messages.error('username must be alpha-numric!')
            return redirect('home')
        myuser= User.objects.create_user(username,email,pass1)
        myuser.first_name =fname
     
    

        
    

        myuser.save()
       


        messages.success(request,"Your account is created" )
        # welcome email
       

        
        
       
       
        return redirect("signin")


    
    
    
    return render(request,"app/signup.html")
def signin(request):
    


    if request.method =="POST":

        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username= username, password= pass1)
        if user is not None:



            login(request,user)
            fname = user.first_name
            return render(request,"app/index.html",{'fname':fname})


        else:

            messages.error(request,"Bad credentials")
            return redirect('home')
   
   
   
   
   
    return render(request,"app/signin.html")
def signout(request):
    logout(request)
    messages.success(request,"logged out succesfullly")
    return redirect('home')

def profile(request):
    
    contex={
        'user':request.user

    }
    return render(request,"app/profile.html")

def company_page(request):
    company = Company.objects.first()
    return render(request, 'app/company_page.html', {'company': company})




def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'app/post_detail.html', {'post': post, 'comments': comments})

def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'app/all_posts.html', {'posts': posts})


    
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user

        post = Post(title=title, content=content, author=author)
        post.save()
        return HttpResponseRedirect('/post/' + str(post.id))
    else:
        return render(request, 'app/create_post.html')


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes.add(request.user)
    return HttpResponseRedirect('/post/' + str(post_id))

def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.dislikes.add(request.user)
    return HttpResponseRedirect('/post/' + str(post_id))

def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        content = request.POST.get('content')
        comment = Comment(post=post, user=request.user, content=content)
        comment.save()
    return HttpResponseRedirect('/post/' + str(post_id))

def change_password(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'app/change-password.html', {
        'form': form
    })