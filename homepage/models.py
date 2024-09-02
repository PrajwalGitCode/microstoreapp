from django.db import models

# Create your models here.

class WatchesUploads(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() 
    price = models.FloatField()
    image = models.ImageField(upload_to="watch_images/")
    updated = models.DateTimeField(auto_now=True)  
    created = models.DateTimeField(auto_now_add=True)


class Watches(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() 
    details = models.TextField(default="coming soon") 
    price = models.FloatField()
    image = models.ImageField(upload_to="all_images/", default='all_images/w_5.png')
    updated = models.DateTimeField(auto_now=True)  
    created = models.DateTimeField(auto_now_add=True)


class Laptop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() 
    details = models.TextField(default="coming soon") 
    price = models.FloatField()
    image = models.ImageField(upload_to="lap_images/", default='lap_images/w_5.png')
    updated = models.DateTimeField(auto_now=True)  
    created = models.DateTimeField(auto_now_add=True)

class Mobile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() 
    details = models.TextField(default="coming soon") 
    price = models.FloatField()
    image = models.ImageField(upload_to="mob_images/", default='mob_images/w_5.png')
    updated = models.DateTimeField(auto_now=True)  
    created = models.DateTimeField(auto_now_add=True)

class Graphic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() 
    details = models.TextField(default="coming soon") 
    price = models.FloatField()
    image = models.ImageField(upload_to="gra_images/", default='gra_images/w_5.png')
    updated = models.DateTimeField(auto_now=True)  
    created = models.DateTimeField(auto_now_add=True)

class Processor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() 
    details = models.TextField(default="coming soon") 
    price = models.FloatField()
    image = models.ImageField(upload_to="pro_images/", default='pro_images/w_5.png')
    updated = models.DateTimeField(auto_now=True)  
    created = models.DateTimeField(auto_now_add=True)

class Accessory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField() 
    details = models.TextField(default="coming soon") 
    price = models.FloatField()
    image = models.ImageField(upload_to="acc_images/", default='acc_images/w_5.png')
    updated = models.DateTimeField(auto_now=True)  
    created = models.DateTimeField(auto_now_add=True)