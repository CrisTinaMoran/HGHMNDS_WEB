from django.db import models
from django.forms import PasswordInput


class Item(models.Model):
    class Color(models.TextChoices):
        RED = 'red', 'Red'
        YELLOW = 'yellow', 'Yellow'
        BLUE = 'blue', 'Blue'
        BLACK = 'black', 'Black'
        WHITE = 'white', 'White'
    
    class Size(models.TextChoices):
        X_SMALL = 'XSmall', 'X-Small'
        SMALL = 'Small', 'Small'
        MEDIUM = 'Medium', 'Medium'
        LARGE = 'Large', 'Large'
        X_LARGE = 'XLarge', 'X-Large'
    
    Item_name = models.CharField(max_length=255, null=True)
    Item_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Specify max_digits and decimal_places
    quantity = models.IntegerField()
    color = models.CharField(max_length=10, choices=Color.choices)  # Use choices for Color
    size = models.CharField(max_length=10, choices=Size.choices)    # Use choices for Size
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Corrected typo from DataTimeField to DateTimeField

    def __str__(self):
        return self.Item_name


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255) 
    is_admin = models.BooleanField(default=False)  
    is_seller = models.BooleanField(default=False)  

    def __str__(self):
        return self.username
