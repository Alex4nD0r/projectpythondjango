from django.shortcuts import render

from .analysis.get_vacancies import get_vacancies
from .models import Demand, Geo, Index, Skills
from .analysis.tables import get_table_data
import os.path
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# Create your views here.


def index_view(request):
    index = Index.objects.all()[0]
    return render(request, 'index.html', {'text': index.text, 'image': index.index_image})


def demand_view(request):
    demand = Demand.objects.all()[0]
    data, rows, cols = get_table_data(os.path.join(BASE_DIR, "dba\\analysis\\report_years.xlsx"))
    return render(request, 'demand.html', {'image': demand.year_dynamics_of_salary_graphic, 'rows': range(rows),
                                           'cols': range(cols), 'data': data, })


def geo_view(request):
    geo = Geo.objects.all()[0]
    data, rows, cols = get_table_data(os.path.join(BASE_DIR, "dba\\analysis\\report_cities.xlsx"))
    return render(request, 'geo.html', {'image': geo.city_dynamics_of_salary_graphic, 'rows': range(rows),
                                        'cols': range(cols), 'data': data, })


def skills_view(request):
    skills = Skills.objects.all()[0]
    data, rows, cols = get_table_data(os.path.join(BASE_DIR, "dba\\analysis\\report_skills.xlsx"))
    return render(request, 'skills.html', {'image': skills.skills_graphic, 'rows': range(rows),
                                           'cols': range(cols), 'data': data})


def vacancies_view(request):
    vacancies = get_vacancies()
    return render(request, 'vacancies.html', {'vacancies': vacancies})