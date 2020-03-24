from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.sites.models import Site
from .models import Profile
from projects.models import Projects
from .forms import userUpdateForm, profileUpdateForm, projectUpdateForm
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.views.generic import UpdateView
# Create your views here.
# ----------------- Registeration(Salah) ------------------------
def register(request):
    if request.method == "POST":
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        username = request.POST['userName']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        picture = request.FILES['pic']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken')
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is taken')
                return redirect("register")
            else:
                user = User.objects.create_user(first_name=first_name , last_name=last_name ,
                                                username=username , email=email ,
                                                password=password1 ,
                                                )
                profile = Profile(phoneNum=phone, user_picture=picture, user=user )
                profile.save()
                user.save()
                
                print("User Registered...")
                return redirect("login")
        else:
            messages.info(request,'Password not matching !!')
            return redirect("register")
    else:
        return render(request,'register.html')
# ----------------- Login(Salah) ------------------------
def login(request):
    if request.method=="POST":
        username = request.POST['userName']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid credentials")
            return redirect("login")
    else:
        return render(request,'login.html')

# ---------------------------------------------------


@login_required()
def show_profile(request):
    # profile = Profile.user
    # phone = profile.phone_set.all()
    return render(request, 'user/profile.html')


@login_required()
def edit_profile(request):
    if request.method == 'POST':
        user_form = userUpdateForm(request.POST, instance=request.user)
        profile_form = profileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully')
            return redirect('/profile')

    else:
        user_form = userUpdateForm(instance=request.user)
        profile_form = profileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'user/edit_profile.html', context)


@login_required()
def delete_profile(request,id):
    if request.method == 'POST':
        # # current_password = request.user.password
        # password = request.POST['password']
        # if check_password(password, encoded=HttpResponse):
        account = User.objects.get(id=id)
        account.delete()
        return render(request, 'register.html')
    else:
        return render(request, 'user/delete_profile.html')


@login_required()
def my_projects(request,id):
    u_project = Projects.objects.filter(user_id=id)
    return render(request, 'user/my_projects.html', {'u_project': u_project})


@login_required()
def delete_project(request, id):
    u_project = Projects.objects.get(id=id)
    u_project.delete()
    # return HttpResponse("Done")
    return render(request, 'user/profile.html')


# @login_required()
# def edit_project(request, id):
#     if request.method == 'POST':
#         u_project = Projects.objects.get(id=id)
#         project_form = projectUpdateForm(request.POST, instance=request.u_project)
#         if project_form.is_valid():
#             project_form.save()
#             messages.success(request, 'Your project has been updated successfully')
#             return redirect('/profile/my_project/{{id}}')
#
#     else:
#         project_form = projectUpdateForm(instance=request.u_project)
#
#     context = {
#         'project_form': project_form,
#     }
#     return render(request, 'user/edit_project.html', context)



