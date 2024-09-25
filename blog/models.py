from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from decimal import Decimal
from django.utils import timezone


class BannerStage(models.Model) :
    title = models.TextField(max_length=30)
    subtitle = models.TextField(max_length=255)

    def __str__(self):
        return self.title

class ServiceStar(models.Model) :
    image = models.ImageField(upload_to='image/', null = True)
    title = models.CharField(max_length=15, null = True)
    body = models.CharField(max_length=100, null = True)

    def __str__(self) -> str:
        return self.title
    
class AboutStage(models.Model) :
    image1 = models.ImageField(upload_to='image/', null = True)
    image2 = models.ImageField(upload_to='image/', null = True)
    image3 = models.ImageField(upload_to='image/', null = True)
    image4 = models.ImageField(upload_to='image/', null = True)
    title = models.CharField(max_length=10, null = True)
    body = models.TextField(null = True)
    footer_number = models.PositiveIntegerField(null =True)
    footer_title = models.CharField(max_length=20, null = True)
    footer_body = models.CharField(max_length=20, null = True)

    def __str__(self) -> str:
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Comment(models.Model) :
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self) -> str:
        return f"{self.author}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class TeamStage(models.Model) :
    image = models.ImageField(upload_to='image/')
    name = models.CharField(max_length=30, null=True) 
    subject = models.CharField(max_length=30, null = True)
    body = models.TextField(null=True)
    facebook = models.CharField(max_length=255, null = True)
    telegram = models.CharField(max_length=255, null = True)
    instagram = models.CharField(max_length=255, null = True) 

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='menu_items/', null=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=30, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_items')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.TextField()
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=0)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    name = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=18, null = True)
    address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if self.quantity and self.item.price:
            self.total_price = Decimal(self.quantity) * self.item.price
        else:
            self.total_price = Decimal(0)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.item.name} - {self.quantity}"
    
class BookingStage(models.Model) :
    name = models.CharField(max_length=20, null=True)
    email = models.EmailField()
    datetime = models.DateTimeField(auto_now_add=True)
    people_quantity = models.CharField(max_length=20, null=True)
    requests = models.TextField()
    

    def __str__(self) -> str:
        return self.name

class BookingMedia(models.Model) :
    video_files = models.FileField(upload_to='media/',null=True)

    def __str__(self) -> str:
        return str(self.video_files)
    
class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_items = models.ManyToManyField(CartItem, null=True, blank=True) 
    name = models.CharField(max_length=300, null=True)
    phone = models.CharField(max_length=18, null=True)
    address = models.TextField()

    
    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"
    
    
# @receiver(post_save, sender=MenuItem)
# def update_MenuItem(sender, instance, **kwargs):
#     menu = MenuItem.objects.get(id=instance.id)
#     menu.image = instance.image
#     menu.save()
