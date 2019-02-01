from django.db import models
from django import forms
from django.urls import reverse
from django.core.validators import MinLengthValidator


# modelform을 쓸 때는 validator를 model.py에 정의해야함
def min_length_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력하시오.')


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_length_3_validator])
    content = models.TextField()
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse('dojo:post_new')


class GameUser(models.Model):
    server_name = models.CharField(max_length=10,
                                   choices=(
                                       ('A', 'A서버'),
                                       ('B', 'B서버'),
                                       ('C', "C서버"),
                                   ))
    username = models.CharField(max_length=20, validators=[MinLengthValidator])

    class Meta:
        unique_together = [
            ('server_name', 'username'),
        ]
