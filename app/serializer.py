from rest_framework import serializers
from .models import Projects, Employee,ProjectDiscription,Skills


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'


class ProjectDiscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDiscription
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'
