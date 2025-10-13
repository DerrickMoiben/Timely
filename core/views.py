from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, BusinessIforForm, CarWashSetupForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import BusinessInfo


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
                return redirect('onboarding')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    context = {'form':form}
    return render(request, 'login.html', context)
                
    
def business_onboarding(request):
    if request.method == 'POST':
        form = BusinessIforForm(request.POST)
        if form.is_valid():
            business = form.save()
            messages.success(request, "You have successfuly registered your Business to Timely")
            """This is a dictonary mapping business tyoes to ther e setup route names for redirection"""
            setup_redirects = {
                'car_wash': 'carwashsetup',
                
            }
            redirect_url =  setup_redirects.get(business.business_type)
            if redirect_url:
                return redirect(redirect_url, business_id=business.id)
            else:
                messages.warning(request, "Unknown business tyoe please contact Cutomer car via 0721170527")
                return redirect('onboarding')
        else:
            messages.error(request, "There was an error while trying  to onaboard you business")
    else:
        form = BusinessIforForm()
    context = {'form':form}
    
    return render(request, 'onboarding.html', context)

def carwashsetup(request, business_id):
    business =  BusinessInfo.objects.get(id=business_id)
    if request.method == 'POST':
        form = CarWashSetupForm(request.POST)
        if form.is_valid():
            carwash = form.save(commit=False)
            carwash.business = business
            carwash.save()
            messages.success(request, "You have successfully Setup you carwash Business with timely")
            return redirect("home")
        else:
            messages.error(request, "There was an error while trying to onboard you business")
    else:
        form = CarWashSetupForm()
    context = {'form':form}
    
    return render(request, 'carwashsetup.html', context)
            