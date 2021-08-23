from django.db import models
from django.contrib.auth.models import User


STATE_CHOICES = (
    ('West Bengal', 'West Bengal'),
    ('Delhi', 'Delhi'),
    ('Maharashtra', 'Maharashtra'),
    ('Karnataka', 'Karnataka'),
    ('Goa', 'Goa'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Bihar', 'Bihar'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Kerala', 'Kerala'),
)

COURSE_CHOICES = (
    ('Bachelor of Technology', 'Bachelor of Technology'),
    ('Bachelor of Arts', 'Bachelor of Arts'),
    ('Bacheor of Science', 'Bachelor of Science'),
    ('Bachelor of Commerce', 'Batchelor of Commerce'),
)

class profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default=' ')
    profile_img = models.ImageField(upload_to='pro_img', blank=True)
    dob = models.DateField()
    mobile_no = models.PositiveIntegerField()
    state = models.CharField(max_length=200, choices=STATE_CHOICES)
    address = models.CharField(max_length=250)
    father_name = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150)
    college_name = models.TextField()
    school_name = models.TextField()
    class_12 = models.FloatField()
    class_10 = models.FloatField()
    persue_course = models.CharField(max_length=150, choices=COURSE_CHOICES)
    language = models.TextField(blank=True)

    def __str__(self):
        return self.name

class skills(models.Model):
    profile = models.OneToOneField(profile, on_delete=models.CASCADE)
    code = models.TextField(default='')
    skill_name = models.CharField(max_length=200)
    intern_exp = models.TextField()
    facebook = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    linkedIn = models.CharField(max_length=150)

    def __str__(self):
        return self.profile.name
    
