from django import forms
from .models import Post




# PostForm을 modelForm으로 구현
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        # fields='__all__'
        fields=['title','content']
#데이터베이스에 대한 인터페이싱이 아니라서 길이제한 지정 필요없음
# class PostForm(forms.Form):
#     title = forms.CharField(validators=[min_length_3_validator])
#     content = forms.CharField(widget=forms.Textarea)
#
#     def save(self,commit=True):
#         # 1
#         # post = Post()
#         # post.title = form.cleaned_data['title']
#         # post.content = form.cleaned_data['content']
#         # post.save()
#
#         # 2
#         # post=Post(title=form.cleaned_data['title'],
#         #           content=form.cleaned_data['content'])
#         # post.save()
#
#         # 3
#         # post=Post.objects.create(title=form.cleaned_data['title'],
#         #                          content=form.cleaned_data['content'])
#         # post.save()
#
#         # 4
#         post=Post(**self.cleaned_data)
#         if commit:
#             post.save()
#         return post