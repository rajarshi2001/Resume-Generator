from django.shortcuts import render, HttpResponseRedirect
from .forms import studentForms, studentDetailForms, studentLoginForm, changePasswordForm, updateEmailForm, skillsForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import profile, skills
from django.contrib.auth.forms import PasswordResetForm

def student_signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            stu = studentForms(request.POST)
            if stu.is_valid():
                messages.success(request, 'Registration Done Successfully')
                stu.save()
                return HttpResponseRedirect('/')
        else:
            stu = studentForms()
        return render(request, 'signup.html', {'stud': stu})
    else:
        return HttpResponseRedirect('/profile/')

def student_login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            forms = studentLoginForm(request=request, data=request.POST)
            if forms.is_valid():
                u_name = forms.cleaned_data['username']
                p_wrd = forms.cleaned_data['password']
                user = authenticate(username=u_name, password=p_wrd)
                if user is not None:
                    messages.success(request, 'Logged In Successfully !!')
                    login(request, user)
                    return HttpResponseRedirect('/profile/')
        else:
            forms = studentLoginForm()
        return render(request, 'login.html', {'forms': forms})
    else:
        return HttpResponseRedirect('/profile/')


def profile_view(request):
    if request.user.is_authenticated:
        if request.user.username == 'admin':
            pro = profile.objects.all()
            return render(request, 'adminPage.html', {'pro': pro})
        else:
            if request.method == 'POST':
                forms = studentDetailForms(request.POST, request.FILES)
                sforms = skillsForm(request.POST)
                if forms.is_valid() and sforms.is_valid():
                    user = request.user
                    forms = forms.save(commit=False)
                    inst = forms.name
                    forms.user = user 
                    forms.save()
                    prol = profile.objects.get(name=inst)
                    sforms = sforms.save(commit=False)
                    sforms.profile = prol
                    sforms.save()
                    messages.success(request, 'Your Profile has been added')
                    return HttpResponseRedirect('/visitProfile/')
            else:
                forms = studentDetailForms()
                sforms = skillsForm()
            return render(request, 'profile.html', {'forms': forms, 'sforms': sforms})
    else:
        return HttpResponseRedirect('/')

def user_profile(request):
    if request.user.is_authenticated:
        uid = request.user.id
        prof = profile.objects.filter(user=uid)
        return render(request, 'resumeList.html', {'prof': prof})
    else:
        return HttpResponseRedirect('/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def resume_view(request, id):
    if request.user.is_authenticated:
        prof = profile.objects.get(pk=id)
        skill = skills.objects.get(profile=prof.id)
        return render(request, 'resume.html', {'prof': prof, 'skill': skill})
    else:
        return HttpResponseRedirect('/')

def update_profile(request, id):
    if request.user.is_authenticated:
        pi = profile.objects.get(pk=id)
        skill = skills.objects.get(profile=pi)
        if request.method == 'POST':
            forms = studentDetailForms(data=request.POST, files=request.FILES, instance=pi)
            sforms = skillsForm(data=request.POST, instance=skill)
            if forms.is_valid() and sforms.is_valid():
                forms = forms.save(commit=False)
                forms.user = request.user
                forms.save()
                inst = forms.name
                sforms = sforms.save(commit=False)
                prol = profile.objects.get(name=inst)
                sforms.profile = prol
                sforms.save()
                return HttpResponseRedirect('/visitProfile/')
        else:
            forms = studentDetailForms(instance=pi)
            sforms = skillsForm(instance=skill)
        return render(request, 'updateResume.html', {'forms': forms, 'sforms': sforms, 'pi': pi})
    else:
        return HttpResponseRedirect('/')

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = changePasswordForm(user=request.user, data=request.POST)
            if forms.is_valid():
                forms.save()
                return HttpResponseRedirect('/')
        else:
            forms = changePasswordForm(user=request.user)
        return render(request, 'changepassword.html', {'forms': forms})
    else:
        return HttpResponseRedirect('/')


def update_email(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            forms = updateEmailForm(data = request.POST, instance=request.user)
            if forms.is_valid():
                forms.save()
                return HttpResponseRedirect('/visitProfile/')
        else:
            forms = updateEmailForm(instance=request.user) 
        return render(request, 'updateEmail.html', {'forms': forms})
    else:
        return HttpResponseRedirect('/')

def delete_view(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = profile.objects.get(pk=id)
            pi.delete()
            pro = profile.objects.all()
        else:
            pro = profile.objects.all()
        return render(request, 'adminPage.html', {'pro': pro})
    else:
        return HttpResponseRedirect('/')
