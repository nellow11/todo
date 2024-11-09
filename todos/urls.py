from . import views
from django.urls import path




urlpatterns = [

    
    path("addTask/", views.addTask , name= "addTask"),
    
    #mark as done and undon 
    path("markasdone/<int:pk>", views.markasdone, name= "markasdone"),
    path("markasundone/<int:pk>", views.markasundone, name= "markasundone"),
    
    #edit and deleate
    path("edittask/<int:pk>/" ,  views.edittask , name = "edittask"),
    path("delete1/<int:pk>/" ,  views.delete1 , name = "delete1"),
    
    
    
]
