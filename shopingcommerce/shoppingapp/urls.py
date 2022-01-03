from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
from django.http import HttpResponse
app_name='cart'
urlpatterns=[
    path('',views.home),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('afterlogin',views.afterlogin),
    path('cart',views.addtocart,name='cart'),
    path('mycart',views.viewmycart,name='viewmycart'),
   
]