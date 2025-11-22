from django.db import models

# Create your models here.
class BusinessInfo(models.Model):
    BUSINESS_TYPE_CHOICES = [
        ('car_wash', 'Car Wash'),
        ('barber', 'Barber Shop'),
        ('spa_salon', 'Spa & Salon'),
        ('gym', 'Gym & Fitness'),
    ]
    name = models.CharField(max_length=100)
    description =  models.TextField()
    business_type =  models.CharField(max_length=50, choices=BUSINESS_TYPE_CHOICES, default='car_wash')
    created_at =  models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    
class CarwashSetup(models.Model):
    business = models.OneToOneField(BusinessInfo, on_delete=models.CASCADE, related_name='carwash_setup')
    
    def __str__(self):
        return f"Carwash Setup for {self.business.name}"
    
    
class BusinessWebsite(models.Model):
    business =  models.OneToOneField(BusinessInfo, on_delete=models.CASCADE, related_name='website')
    theme_color =  models.CharField(max_length=20, default='#28a745')
    about = models.TextField(blank=True)
    services = models.TextField(blank=True)
    pricing_details = models.TextField(help_text="Provide pricing details for different services", default='10')
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True, default='13')
    location = models.CharField(max_length=255,  default='nairobi')
    closing_time = models.TimeField(default='10')
    
    def __str__(self):
        return f"Website for {self.business.name}"
