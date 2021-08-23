from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm, PasswordResetForm, SetPasswordForm
from .models import profile, skills
from django.utils.translation import gettext, gettext_lazy as _

class studentForms(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password(Again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email',]
        labels = {'first_name': 'First Name', 'last_name': 'Last Name', 'username': 'Username', 'email': 'Email Address'}
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control'}), 
        'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'username': forms.TextInput(attrs={'class': 'form-control'}) }

class studentLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class studentDetailForms(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['name', 'father_name', 'mother_name', 'dob', 'mobile_no', 'state',  'address', 'college_name', 'school_name', 'class_12', 'class_10', 'language', 'persue_course',  'profile_img']
        labels = {'class_12': 'Percentage in Class XII', 'class_10': 'Percentage in class X'}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}), 'father_name': forms.TextInput(attrs={'class': 'form-control'}), 'mother_name': forms.TextInput(attrs={'class': 'form-control'}),'dob': forms.DateTimeInput(attrs={'class': 'form-control'}),
        'mobile_no': forms.NumberInput(attrs={'class': 'form-control'}), 'state': forms.Select(attrs={'class': 'form-control'}), 
        'address': forms.TextInput(attrs={'class': 'form-control'}), 'college_name': forms.TextInput(attrs={'class': 'form-control'}),
        'school_name': forms.TextInput(attrs={'class': 'form-control'}), 'class_12': forms.NumberInput(attrs={'class': 'form-control'}), 'class_10': forms.NumberInput(attrs={'class': 'form-control'}), 'language': forms.Textarea(attrs={'class': 'form-control'}),
        'persue_course': forms.Select(attrs={'class': 'form-control'}), 'profile_img': forms.ClearableFileInput(attrs={'class': 'form-control'})}

class skillsForm(forms.ModelForm):
    class Meta:
        model = skills
        fields = ['code', 'skill_name', 'intern_exp', 'facebook', 'instagram', 'linkedIn']
        labels = {'coding': 'Programming Languages(if any)', 'skill_name': 'Specialized Skills', 'intern_exp': 'Internships(if any)'}
        widgets = {'code': forms.Textarea(attrs={'class': 'form-control'}), 'skill_name': forms.TextInput(attrs={'class': 'form-control'}),
        'intern_exp': forms.Textarea(attrs={'class': 'form-control'}), 'facebook': forms.TextInput(attrs={'class': 'form-control'}),
        'instagram': forms.TextInput(attrs={'class': 'form-control'}), 'linkedIn': forms.TextInput(attrs={'class': 'form-control'})}

class changePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password(Again)', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class updateEmailForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['email']
        labels = {'email': 'Change Email Address'}
        widgets = {'email': forms.EmailInput(attrs={'class': 'form-control'})}

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Enter Your Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'
    , 'class': 'form-control'}))
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'
    , 'class': 'form-control'}))