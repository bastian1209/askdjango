from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='shop_post_set')
    message=models.TextField()
    updated_at=models.DateTimeField(auto_now=True)