from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print('nimefika hapa but siwezi save')
            messages.success(request, 'You have sucessfully created an a ccount with timely')
            return redirect('login')
        else:
            print(form.errors)
            messages.error(request, 'Their was an error while trying to create your account')
            
    else:
        form = SignupForm()
            
    return render(request, 'signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username =  form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have logged in successfully')
                return redirect('homepage')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    context = {'form':form}
    return render(request, 'login.html', context)
                
        