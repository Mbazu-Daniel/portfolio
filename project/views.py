from django.shortcuts import render
from .models import Project, Experience, Skill

# Create your views here.
def index(request):
    projects = Project.objects.all()
    experience = Experience.objects.all()
    skill = Skill.objects.all()
    context ={
        'projects': projects,'experience':experience, 'skill':skill
    }
    return render(request, 'project/index.html', context)

