from . import views
from django.urls import path
app_name = 'learningapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='registers'),
    path('login',views.login,name='login'),
   
    
]