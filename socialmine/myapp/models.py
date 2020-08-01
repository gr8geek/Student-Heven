from django.db import models
class user(models.Model):
    name = models.CharField(max_length=100)
    dob= models.DateField()
    email = models.EmailField()
    #phone = models.CharField(max_length=100)
    gender = models.CharField(max_length=1,default="")

    uname = models.CharField(primary_key=True,max_length=60)
    password=models.CharField(max_length=100)
    #image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name+"   UNAME::"+self.uname
