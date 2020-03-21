from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.last_five_project, name="home"),
    path('category/<int:id>', views.category_details, name="ProjectCategory"),
]