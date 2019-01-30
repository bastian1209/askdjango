from django import forms


def min_length_3_validator(value):
    if len(value)<3:
        raise forms.ValidationError('3글자 이상 입력하시오.')

#데이터베이스에 대한 인터페이싱이 아니라서 길이제한 지정 필요없음
class PostForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea)
