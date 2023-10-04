from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category,UserProfile
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy

class HomeView(ListView):
	model=Post
	template_name='home.html'
	ordering=['-created_on']

class BlogDetailView(DetailView):
	model=Post
	template_name='blogdetail.html'

def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('home')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, 'register.html', context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('home')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, 'login.html', context={"login_form":form})

#CRUD OPERATIONS

class AddPostView(CreateView):
	model=Post
	template_name='createblog.html'
	fields=['title','author','body']
	success_url=reverse_lazy('home')

class UpdatePostView(UpdateView):
	model=Post
	template_name='updatepost.html'
	fields=['title','author','body']
	success_url=reverse_lazy('home')

class DeletePostView(DeleteView):
	model=Post
	template_name='deletepost.html'
	#fields=['title','author','body']
	success_url=reverse_lazy('home')

# Create your views here.
