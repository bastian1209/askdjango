from django.db import models
import re
from django.forms import ValidationError
from django.conf import settings
from django.urls import reverse

def lnglat_validator(value):
    if not re.match(r'^([+-]?\d+\.?\d*),([+-]?\d+\.?\d*)$',value):
        raise ValidationError('Invalid lng lat format')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d',"Draft"),
        ('p','Published'),
        ('w','withdrawn')
    )
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='blog_post_set')
    author = models.CharField(max_length=20)
    title = models.CharField(max_length=100,verbose_name='제목',help_text='포스팅 제목을 입력해주세요. 100자 이내.') # 길이 제한 str
    content = models.TextField(verbose_name='내용')
    tags = models.CharField(max_length=100, blank = True)
    lnglat = models.CharField(max_length = 50,
                              blank = True,
                              validators=[lnglat_validator],
                              help_text = '위도/경도 포맷으로 입력하시오.')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    tag_set=models.ManyToManyField('Tag') #relation의 대상이 뒤에 정의 되어 있으면 문자열로 지
    created_at = models.DateTimeField(auto_now_add = True) #최초 생성시 시간 저장
    updated_at = models.DateTimeField(auto_now = True)     #갱신마다 시간 저장

    class Meta:
        ordering= ['-id']

    #object로 말고 실제 내용을 보여주기 위해
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.id])

class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    author=models.CharField(max_length=20)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name=models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
