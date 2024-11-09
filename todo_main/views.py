


from django.shortcuts import render
from todos.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed = False).order_by("-updated")
    is_completed = Task.objects.filter(is_completed= True)
    
    context = {
        
        "tasks" : tasks,
        "is_completed" : is_completed,
        
    }
        
    
    return render (request,"home.html ", context)