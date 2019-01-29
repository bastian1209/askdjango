from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    # username=models.CharField(max_length=20)
    # email=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    # date_joined=models.DateTimeField(auto_now_add=True)
