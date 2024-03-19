from . import views
from django.urls import path
app_name = 'learningapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('allProCat',views.allProCat,name='allProCat'),
    path('<slug:c_slug>/',views.allProCat,name='course_by_categoryr')
   
    
]