
from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    
    path("admin/", admin.site.urls),
    path("", views.home , name="home"),
    
    path("todos/", include("todos.urls")),
    
]
