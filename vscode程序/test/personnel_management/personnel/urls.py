from django.urls import path, re_path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('register/',views.register,name='register'),
    # path('index/', views.index, name='index'),
    path('append_user/', views.append_user, name='append_user'),
    path('user_list/', views.user_list, name='user_list'), 
    # path('view_people/', views.view_people, name='view_people'),
    # path('update_person/<int:person_id>/',views.update_person,name='update_person'),
    
]