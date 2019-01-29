from django.urls import path
from . import views

urlpatterns=[
    #최상위 주소
    path('',views.post_list),
    path('<int:pk>/',views.post_detail)
]