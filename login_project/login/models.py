from django.db import models

# Create your models here.

class Login(models.Model):
 
    f_name=models.CharField(max_length=200,null=False,blank=False)
    l_name=models.CharField(max_length=200,null=False,blank=False)
    email=models.EmailField(max_length=200,null=False,blank=False)



    def __str__(self):
        return self.f_name
