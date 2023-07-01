from django.db import models


class Hobby(models.Model):

    def __str__(self):
        return self.hobby_name

    hobby_name = models.CharField(max_length=200)
    hobby_description = models.CharField(max_length=200)
    skill_level = models.IntegerField()
    hobby_image = models.CharField(max_length=2000, default='https://clipart-library.com/img/48366.jpg')


class Project(models.Model):

    def __str__(self):
        return self.project_name

    project_name = models.CharField(max_length=200)
    project_description = models.CharField(max_length=200)
    project_link = models.CharField(max_length=300)
    project_image = models.CharField(max_length=2000, default='https://www.pngitem.com/pimgs/m/302-3024031_projects-icon-png-skills-icon-for-resume-png.png')
