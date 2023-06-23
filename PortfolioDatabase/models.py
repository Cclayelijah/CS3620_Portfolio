from django.db import models


class Hobby(models.Model):

    def __str__(self):
        return self.hobby_name

    hobby_name = models.CharField(max_length=200)
    hobby_description = models.CharField(max_length=200)
    skill_level = models.IntegerField()


class Project(models.Model):

    def __str__(self):
        return self.project_name

    project_name = models.CharField(max_length=200)
    project_description = models.CharField(max_length=200)
    project_link = models.CharField(max_length=300)