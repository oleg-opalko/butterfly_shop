from django.core.validators import RegexValidator
from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Contact from {self.name}'

class ContactUs(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?3?\d{9,15}',
                                 message="Phone number must be entered in the format: '+3999999999'")
    country = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, validators=[phone_regex])

    def __str__(self):
        return f'Contact us: {self.country} {self.address} {self.phone}'
