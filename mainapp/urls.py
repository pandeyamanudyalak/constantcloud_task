from django.urls import path
from mainapp import views

urlpatterns = [
    path('',views.index),
    path('user_login',views.user_login),
    path('create_marksheet', views.create_marksheet),
    path('student_list', views.student_list),
    path('student_data', views.student_data),
    path('user_register',views.user_register)
]
