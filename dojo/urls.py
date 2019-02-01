from django.conf.urls import url
from . import views
from . import views_cbv
from django.urls import path

app_name='dojo'

urlpatterns=[
    url(r'^sum/(?P<numbers>[\d/]+)/$',views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$',views.hello),

    url(r'^post_list1/$',views.post_list1),
    url(r'^post_list2/$',views.post_list2),
    url(r'^post_list3/$',views.post_list3),
    url(r'^excel_downloader/$',views.excel_downloader),

    url(r'^cbv/post_list1/$', views_cbv.post_list1),
    url(r'^cbv/post_list2/$', views_cbv.post_list2),
    url(r'^cbv/post_list3/$', views_cbv.post_list3),
    url(r'^cbv/excel_downloader/$', views_cbv.excel_downloader),
    path('new/',views.post_new),
]