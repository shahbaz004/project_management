from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Projects, Employee, ProjectDiscription, Skills
from .serializer import ProjectSerializer, EmployeeSerializer, ProjectDiscriptionSerializer, SkillsSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer



class ProjectDiscriptionViewSet(ModelViewSet):
    queryset = ProjectDiscription.objects.all()
    serializer_class = ProjectDiscriptionSerializer




class SkillViewSet(ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer


