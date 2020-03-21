from django.shortcuts import render, HttpResponse
from .models import Projects , Report ,Comment
from .form import CommentForm ,ReportForm
# Create your views here.


def listProjects(req):
    context = {
        'projects': Projects.objects.all,
        'activate': 'projects',
    }
    return render(req, 'projects/projects.html', context)


# def singleProject(req, project_id):
#     current_project = Projects.objects.get(id = project_id)
#     context = {
#         'project' : current_project,
#         'similar' : Projects.objects.filter(tag__in=current_project.tag.all)
#     }
#     print(current_project.tag__tag_name)
#     return render(req, 'projects/singleProject.html', context)

def tagProjects(req , tag_name):
    context = {
        'projects' : Projects.objects.filter(tag__tag_name=tag_name),
        'tag' : tag_name
    }
    # print(context['project'])
    return render(req, 'projects/tagProjects.html', context)


def selectProject(req,id):
    project = Projects.objects.filter(id = int(id)).first()
    comments = Comment.objects.filter(project_id=project)
    comment = None
  
    if project:
        if req.method == 'POST':
            comment_form = CommentForm(req.POST)
            if comment_form.is_valid():
                comment_content=req.POST.get("comment_content")
           
                comment=Comment.objects.create(project_id=project,comment_content=comment_content)
                comment.save()
              
        else:
            comment_form = CommentForm()
            
        return render(req,"projects/singleProject.html",{ "project" :project,
        "comments":comments,
        "comment_form":comment_form,
       })

    else:
        return HttpResponse("404 Not Found")

def reportProject(req ):
    project = Projects.objects.filter()
    reports = Report.objects.filter()
    if req.method == 'POST':
            report_form = ReportForm(req.POST or None)
            if report_form.is_valid():
                report_content=req.POST.get("report_content")
            
                report=Report.objects.create(project_id=project,report_content=report_content)
                report.save()
                
    else:
        report_form = ReportForm()
            
    return render(req,"projects/report.html",{
        "reports":reports,
    "report_form":report_form,
   })

