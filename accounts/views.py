from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
# Create your views here.
def profile(request):
    return render(request,'a ccounts/profile.html')

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form=UserCreationForm()
    return render(request,'accounts/signup_form.html',{
        'form':form,
    })