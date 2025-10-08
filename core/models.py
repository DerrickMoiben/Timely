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
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address =  models.TextField()
    business_type =  models.CharField(max_length=50, choices=BUSINESS_TYPE_CHOICES, default='car_wash')
    created_at =  models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    
