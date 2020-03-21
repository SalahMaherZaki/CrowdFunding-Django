from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile,UserPhone
from projects.models import Projects
from .forms import userUpdateForm, profileUpdateForm
from django.contrib import messages

# Create your views here.


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
        account = User.objects.get(id=id)
        account.delete()
        return render(request, 'user/register.html')
    else:
        return render(request, 'user/delete_profile.html')


@login_required()
def my_projects(request,id):
    u_project = Projects.objects.filter(user_id=id)
    return render(request, 'user/my_projects.html', {'u_project': u_project})
