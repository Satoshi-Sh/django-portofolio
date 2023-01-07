from django.shortcuts import render
from projects.models import Project

# Create your views here.

def index(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request,'projects/index.html',context)


def detail(request,pk):
    project = Project.objects.get(pk=pk)
    context= {
        'project':project
    }
    return render(request, 'projects/detail.html',context)