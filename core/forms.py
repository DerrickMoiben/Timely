from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import BusinessInfo, CarwashSetup, BusinessWebsite

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
        model =  CarwashSetup
        exclude = ['business']
        
class BusinessWebsiteForm(forms.ModelForm):
    class Meta:
        model = BusinessWebsite
        exclude = ['business']