from django.db import models

# Create your models here.
class gender(models.Model):
     gender=models.CharField(max_length=7)

     def __str__(self):
          return self.gender

class ATM(models.Model):
     name=models.CharField(max_length=32)
     account_no=models.IntegerField(unique=True)
     phone=models.PositiveIntegerField()
     email=models.EmailField()
     aadhar=models.PositiveIntegerField()
     dob=models.DateField()
     photo=models.ImageField(upload_to='images')
     amount=models.IntegerField(default=500)
     gender=models.ForeignKey(gender,on_delete=models.CASCADE)
     pin=models.IntegerField(default=0)