from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from .forms import LoginForm
app_name='accounts'

urlpatterns=[

    path('signup/',views.signup, name='signup'),
    path('login/',auth_views.LoginView.as_view(),name='login',
         kwargs={
             'template_name': 'registration/login.html',
             'authentication_form':LoginForm,
         }),
    path('logout/',auth_views.LogoutView.as_view(),name='logout',
         kwargs={'next_page':settings.LOGIN_URL}),
    path('profile/',views.profile,name='profile'),
]

