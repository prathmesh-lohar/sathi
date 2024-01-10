from django.db import models

# Create your models here.


class income(models.Model):
    range = models.CharField(max_length=50, blank=True, null=True, default="")
    def __str__(self):
        return str(self.range)
    
class height(models.Model):
    height = models.CharField(max_length=50, blank=True, null=True, default="")
    
    def __str__(self):
        return str(self.height)
    
class color(models.Model):
    color = models.CharField(max_length=50, blank=True, null=True, default="")
    
    def __str__(self):
        return str(self.color)
    
class Qualification(models.Model):
    nameofQualification = models.CharField(max_length=50, blank=True, null=True, default="")
    
    def __str__(self):
        return str(self.nameofQualification)
    
class work(models.Model):
    nameofwork = models.CharField(max_length=50, blank=True, null=True, default="")
    def __str__(self):
        return str(self.nameofwork)
    
class experience(models.Model):
    experience = models.CharField(max_length=50, blank=True, null=True, default="")
    
    def __str__(self):
        return str(self.experience)
    
class hobbies(models.Model):
    nameofhobbie = models.CharField(max_length=50, blank=True, null=True, default="")
    
    def __str__(self):
        return str(self.nameofhobbie)
    
    
class medical_condition(models.Model):
    medical_condition = models.CharField(max_length=50, blank=True, null=True, default="")
    def __str__(self):
        return str(self.medical_condition)
    
class city(models.Model):
    nameofcity = models.CharField(max_length=50, blank=True, null=True, default="")
    def __str__(self):
        return str(self.nameofcity)