from django.shortcuts import render, HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.

from projects.models import Projects, Category


# def all_projects (request):
#     all_projects = Projects.objects.all()
#
#     context ={
#
#         "allProjects":all_projects
#     }
#     return render(request,"homepage.html",context)


def last_five_project(request):
    last_five = Projects.objects.all().order_by("-id")[:5]
    categories_name = Category.objects.all()
    all_projects = Projects.objects.all()

    context = {

        "last_project": last_five,
        "category_name": categories_name,
        "allProjects": all_projects
    }

    return render(request, "homepage.html", context)


def category_details(request, id):
    projects = Projects.objects.filter(category_id=int(id))
    return render(request, "projectDetails.html", {"projects": projects})
