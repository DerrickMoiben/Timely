from django.urls import path
from . import views



urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('onboarding/', views.business_onboarding, name='onboarding'),
    path('carwashsetup/<int:business_id>/', views.carwashsetup, name='carwashsetup'),
    path('businesswebsite/<int:business_id>/', views.businesswebsite, name='businesswebsite'),
]