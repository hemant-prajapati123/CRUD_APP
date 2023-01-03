from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('addstudent',views.addstudent,name="addstudent"),
    path('showstudent',views.showstudent,name="showstudent"),
    path('delete',views.deletestudent,name="sdedstudent"),
]
