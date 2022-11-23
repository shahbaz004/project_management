from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    designation = models.TextField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    skills = models.ManyToManyField("Skills", related_name="skills")
    is_lead = models.BooleanField()
    team_lead = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="lead")
    assigned_project = models.ForeignKey("Projects", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Projects(models.Model):
    project_lead = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, related_name="project_lead")
    working_employee = models.ManyToManyField(Employee, related_name='working_employee')
    delivery_time = models.DateTimeField()
    project_details = models.ForeignKey("ProjectDiscription", on_delete=models.CASCADE, null=False)
    project_budget = models.IntegerField()
    is_completed = models.BooleanField()


class ProjectDiscription(models.Model):
    project_doc = models.URLField()
    project_design = models.URLField()
    project_remark = models.TextField()
    project = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f"{self.project}"


class Skills(models.Model):
    skill = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return f"{self.skill}"
