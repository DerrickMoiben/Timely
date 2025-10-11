from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import BusinessInfo, CarwashSetup

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',   'email']
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    
class BusinessIforForm(forms.ModelForm):
    class Meta:
        model = BusinessInfo
        fields =  '__all__'
        
class CarWashSetupForm(forms.ModelForm):
    class Meta:
        models =  CarwashSetup
        fields = '__all__'