from django.shortcuts import render,get_object_or_404, redirect
from .models import Post
from django.http import Http404
from .forms import PostForm
from django.contrib import messages

# Create your views here.
def post_list(request):
    qs=Post.objects.all()

    q=request.GET.get('q','')
    if q:
        qs= qs.filter(title__icontains=q)
    return render(request, 'blog/post_list.html',{
        'post_list':qs,
        'q':q,
    })

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{
        'post':post,
    })

def post_new(request):
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save()
            messages.success(request,'새 포스팅을 저장했습니다.')
            return redirect(post) #post.get_absolute_url
    else:
        form=PostForm()

    return render(request,'blog/post_form.html',{
        'form':form,
    })

def post_edit(request,id):
    post=get_object_or_404(Post,id=id )
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post=form.save()
            messages.success(request,'포스팅 수정을 완료했습니')
            return redirect(post) #post.get_absolute_url
    else:
        form=PostForm(instance=post)

    return render(request,'blog/post_form.html',{
        'form':form,
    })
