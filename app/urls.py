from django.urls import path, include
from .views import ProjectViewSet, EmployeeViewSet,ProjectDiscriptionViewSet, SkillViewSet
from rest_framework.routers import DefaultRouter

router_master = DefaultRouter()
router_master.register('employee', EmployeeViewSet, basename='employee')
router_master.register('project', ProjectViewSet, basename='project')
router_master.register('projectdiscription', ProjectDiscriptionViewSet, basename='projectdiscription')
router_master.register('skill', SkillViewSet, basename='skill')

urlpatterns = [
    path('', include(router_master.urls)),
]

urlpatterns += router_master.urls


