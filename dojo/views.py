from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import os
from .forms import PostForm
from .models import Post
#FBV
def post_new(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        # is_valid : 모든 vaildator 결과 참이어야 참
        if form.is_valid():
            post=form.save()

            return redirect('/dojo/')

    else:
        form =PostForm()
    return render(request,'dojo/post_form.html',{
        'form':form,
    })

def mysum(request,numbers):
    #HTTP request
    numbers=list(map(lambda x:int(x or 0),numbers.split('/')))
    return HttpResponse(sum(numbers))

def hello(request,name,age):
    return HttpResponse('안녕하세요 {}. {}살이시네요'.format(name,age))

def post_list1(request):
    name='유승룡'
    return HttpResponse('''
    <h1>AskDjango</h1>
    <p>{name}</p>
    '''.format(name=name))

def post_list2(request):
    name = '유승룡'
    return render(request,'dojo/post_list2.html',{'name':name})

def post_list3(request):
    return JsonResponse({
        'message':'안녕하세요',
        'items':['python','django','Celery','Azure','AWS']
    },json_dumps_params={'ensure_ascii':False})

def excel_downloader(request):
    filepath='/Users/ryong/Downloads/test.xlsx'
    filename=os.path.basename(filepath)
    with open(filepath,'rb') as f:
        response=HttpResponse(f,content_type='application/vnd.ms-excel')
        response['content-disposition']='attachment;filename="{}"'.format(filename)
        return response

