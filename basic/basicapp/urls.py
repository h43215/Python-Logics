from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index, name="index"),
    path('student/',views.Create_Student,name = "student"),
    path('tc/',views.create_teacher,name="tc"),
    path('principal/', views.principal,name ="principal")
    
]