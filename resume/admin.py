from django.contrib import admin
from .models import profile, skills

@admin.register(profile)
class profileAdmin(admin.ModelAdmin):
       list_display = ['id', 'user', 'name', 'father_name', 'mother_name', 'dob', 'mobile_no', 'state',  'address', 'college_name', 'school_name', 'class_12', 'class_10', 'persue_course',  'profile_img',
    ]
    

@admin.register(skills)
class skillAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'code', 'skill_name', 'intern_exp', 'facebook', 'instagram', 'linkedIn']