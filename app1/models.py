from django.db import models
from django.contrib.auth.models import User
from datetime import date

from django.contrib.auth.models import AbstractUser
# Create your models here.


class profile(models.Model):
    registerfor = models.CharField(max_length=50,default="", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=50,default="", null=True, blank=True)
    lookingfor = models.TextField(default="", null=True, blank=True)
    
    mobile = models.CharField(max_length=50,default="", null=True, blank=True)
    marrital_status = models.CharField(max_length=50,default="", null=True, blank=True)
    dob = models.DateField(auto_now=False, auto_now_add=False , blank=True, null=True)
    height = models.CharField(max_length=50,default="", null=True, blank=True)
    color = models.CharField(max_length=50,default="", null=True, blank=True)
    Qualification = models.CharField(max_length=255,default="", null=True, blank=True)
    work = models.CharField(max_length=50,default="", null=True, blank=True)
    experience = models.CharField(max_length=50,default="", null=True, blank=True)
    hobbies = models.CharField(max_length=255,default="", null=True, blank=True)
    income = models.CharField(max_length=50,default="", null=True, blank=True)
    medical_condition = models.CharField(max_length=50,default="", null=True, blank=True)
    city = models.CharField(max_length=50,default="", null=True, blank=True)
    about_me = models.TextField(null=True,blank=True,default="")
    related_officer = models.CharField(max_length=50,default="", null=True, blank=True)

    username =   models.CharField(max_length=100,default="", null=True, blank=True)
    first_name =   models.CharField(max_length=100,default="", null=True, blank=True)
    last_name =   models.CharField(max_length=100,default="", null=True, blank=True)


    is_featured = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    is_mail_verified = models.BooleanField(default=False)
    
    views = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)
    
    def calculate_profile_completion(self):
        total_fields = 18  # Assuming 18 fields in your model (update accordingly)
        completed_fields = sum(field is not None and field != "" for field in [
            self.registerfor, self.gender, self.lookingfor, self.mobile,
            self.marrital_status, self.dob, self.height, self.color,
            self.Qualification, self.work, self.experience, self.hobbies,
            self.income, self.medical_condition, self.city, self.about_me,
            self.related_officer
        ])

        # Calculate the completion percentage
        if total_fields > 0:
            completion_percentage = (completed_fields / total_fields) * 100
            return round(completion_percentage, 2)
        else:
            return 0.0
    
    @property
    def age(self):  
         if(self.dob != None):
              age = date.today().year - self.dob.year
              return age
    

class family_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    father_name = models.CharField(max_length=50,default="", null=True, blank=True)
    
    father_education = models.CharField(max_length=50,default="", null=True, blank=True)
    father_occupation = models.CharField(max_length=50,default="", null=True, blank=True)
    mother_name = models.CharField(max_length=50,default="", null=True, blank=True)
    mother_education = models.CharField(max_length=50,default="", null=True, blank=True)
    mother_occupation = models.CharField(max_length=50,default="", null=True, blank=True)
    sister=models.TextField(null=True,blank=True, default="")
    brother=models.TextField(null=True,blank=True, default="")
    native_place=models.TextField(null=True,blank=True,default="")
    relatives=models.TextField(null=True,blank=True,default="")

    username =   models.CharField(max_length=100,default="", null=True, blank=True)
    first_name =   models.CharField(max_length=100,default="", null=True, blank=True)
    last_name =   models.CharField(max_length=100,default="", null=True, blank=True)



    def __str__(self):
        return str(self.user)
    

class media(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    dp = models.ImageField(upload_to="dp", height_field=None, width_field=None, max_length=None)

    username =   models.CharField(max_length=100,default="", null=True, blank=True)
    first_name =   models.CharField(max_length=100,default="", null=True, blank=True)
    last_name =   models.CharField(max_length=100,default="", null=True, blank=True)

    def __str__(self):
            return str(self.user)


    
class gallery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    img = models.ImageField(upload_to="gallery", height_field=None, width_field=None, max_length=None)

    def __str__(self):
            return str(self.user)
        
        
class document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    file = models.ImageField(upload_to="documents", height_field=None, width_field=None, max_length=None)
    name = name = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
            return str(self.user)