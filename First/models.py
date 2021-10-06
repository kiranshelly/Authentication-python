from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField


# Create your models here.
class Register(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Username=models.CharField(max_length=20)
    Passcode=models.IntegerField(null=True)
    Number=models.IntegerField(null=True)
    Image=models.ImageField(upload_to='images/%Y/%m/%d/',null=True,blank=True)
    Gender=CharField(max_length=6,null=True)
    Singer=CharField(max_length=10,null=True)

    def __str__(self):
        return f"{self.Username}"

class OTP(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Name = models.ForeignKey(Register, on_delete=models.CASCADE,null=True)
    user_otp=models.IntegerField(null=True)

    def __str__(self):
        return f"User {self.user_otp}"



