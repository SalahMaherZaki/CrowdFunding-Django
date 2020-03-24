from django.shortcuts import render, HttpResponse, redirect
from .models import Projects, Donation, Tag, Report, Comment
from .form import CommentForm, ReportForm
from django.urls import reverse
from django.http import JsonResponse

import stripe

stripe.api_key = 'sk_test_kQeGPyzUEtnwIWuGkSSnkEYy00MTZcMDFF'
# publishkey 'pk_test_qldeOx2RsqvPXmVGAlXBlZQQ00qufvfDcj'


def listProjects(req):
    context = {
        'projects': Projects.objects.all,
        'activate': 'projects',
    }
    return render(req, 'projects/projects.html', context)

def singleProject(req, **kwargs):
    print(kwargs)
    this_project_id = kwargs['project_id']
    current_project = Projects.objects.get(id=this_project_id)
    tags_id = [t.id for t in current_project.tag.all()]
    comments = Comment.objects.filter(project_id=current_project)
    comment = None

    if current_project:
        if req.method == 'POST':
            comment_form = CommentForm(req.POST)
            if comment_form.is_valid():
                comment_content = req.POST.get("comment_content")

                comment = Comment.objects.create(
                    project_id=current_project, comment_content=comment_content)
                comment.save()

        else:
            comment_form = CommentForm()

        current_donation = 20
        # uncomment this and comment the above
        # current_donation = sum(int(money) for money in [donation_value for donation_value in Donation.objects.filter(project_id=this_project_id)])

        context = {
            'project': current_project,
            'activate': 'projects',
            'similar': Projects.objects.filter(tag__in=tags_id).distinct()[:5],
            "comments": comments,
            "comment_form": comment_form,
            "total_donation" : current_donation,
            "donation_percent" : current_donation / current_project.total_donation * 100
        }

        if 'success' in kwargs:
            context['success'] = True

        return render(req, 'projects/singleProject.html', context)
    return HttpResponse("404 Not Found")


def tagProjects(req, tag_name):
    context = {
        'projects': Projects.objects.filter(tag__tag_name=tag_name),
        'tag': tag_name
    }
    return render(req, 'projects/tagProjects.html', context)


def charge(req):

    amount = int(req.POST['amount'])
    project_id = req.POST['project_id']
    # customer = stripe.Customer.create(
    #     source=req.POST['stripeToken']
    # )

    donation = Donation(
        project_id= Projects.objects.get(id=project_id),
        user_id=req.user, # add current user here if this didnt work
        donation_amount=amount*100
    )
    donation.save()

    return redirect(f"/projects/{project_id}/s")


def reportProject(req):
    project = Projects.objects.filter()
    reports = Report.objects.filter()
    if req.method == 'POST':
        report_form = ReportForm(req.POST or None)
        if report_form.is_valid():
            report_content = req.POST.get("report_content")

            report = Report.objects.create(
                project_id=project, report_content=report_content)
            report.save()

    else:
        report_form = ReportForm()

    return render(req, "projects/report.html", {
        "reports": reports,
        "report_form": report_form,
    })
