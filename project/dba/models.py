from django.db import models
import os.path
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
# Create your models here.


class Index(models.Model):
    text = models.TextField()
    index_image = models.ImageField(upload_to='media/', null=True)


class Demand(models.Model):
    year_dynamics_of_salary_graphic = models.ImageField(upload_to='media/')


class Geo(models.Model):
    city_dynamics_of_salary_graphic = models.ImageField(upload_to='media/')


class Skills(models.Model):
    skills_graphic = models.ImageField(upload_to='media/')