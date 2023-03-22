from django.db import models

# Create your models here.
class Car(models.Model):
    name= models.CharField(max_length=200)
    description= models.TextField(null=True,blank=True)
    price= models.TextField(null=True,blank=True)
    year= models.TextField(null=True,blank=True)
    model= models.TextField(null=True,blank=True)
  #  updated = models.DateTimeField(auto_now=True)
   # created=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

#class Meta:
 #   ordering=['-updated','-created']

    def __str__(self):
        return self.name