from rest_framework import serializers
from .models import Projects, Employee, ProjectDiscription, Skills


class ProjectDiscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDiscription
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


# class skill(serializers.Serializer):
#     skill = serializers.CharField()


class EmployeeSerializer(serializers.ModelSerializer):
    # skills = serializers.SlugRelatedField(many=True, read_only=True, slug_field="skill")
    # skills = serializers.StringRelatedField(many=True)
    skills = SkillsSerializer(many=True)

    # team_lead = serializers.RelatedField(source='lead', read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
        # fields = ["name", "designation", "salary", "is_lead", "team_lead", "assigned_project", "skills"]

    def create(self, validated_data):
        skills = validated_data.pop('skills')
        # skills = Employee.objects.get(validated_data)
        instance = Employee.objects.create(**validated_data)
        Employee.objects.create(skills=skills, Employee=instance)
        return instance


class ProjectSerializer(serializers.ModelSerializer):
    working_employee = serializers.CharField(source="working_employee.name", read_only=True)

    class Meta:
        model = Projects
        fields = "__all__"
        # fields = ["project_lead", "working_employee", "delivery_time", "project_details", "project_budget",
        #           "is_completed"]
