import os

from django.shortcuts import render

# Create your views here.

def Themes(request):
    file_path = os.path.join(os.path.dirname(__file__), 'Lessons/lessons.txt')
    with open(file_path, 'r') as f:
        lessons = list(f.read().split())
    print(lessons)
    return render(request,template_name='Themes.html',context={'lessons':lessons})



        