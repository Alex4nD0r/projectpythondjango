from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("demand/", views.demand_view, name="demand"),
    path("geo/", views.geo_view, name="geo"),
    path("skills/", views.skills_view, name="skills"),
    path("vacancies/", views.vacancies_view, name="vacancies")
]