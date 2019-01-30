from django.urls import path
from . import views

app_name='blog' #include에 namespace인자를 주면 urls.py에 app_name을 명시해줘야함

urlpatterns=[
    #최상위 주소
    path('',views.post_list,name='post_list'),
    path('<int:pk>/',views.post_detail,name='post_detail')
]