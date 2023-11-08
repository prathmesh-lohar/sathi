from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from extra.models import city,color,income,height,Qualification,work,experience,hobbies,medical_condition

admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Panel Portal"
admin.site.index_title = "Welcome to Admin Panel Portal"

# Register your models here.
# admin.site.register(profile)


@admin.register(height)
class heightAdmin(ImportExportModelAdmin):
    pass
 

@admin.register(color)
class hcolorAdmin(ImportExportModelAdmin):
    pass
 


@admin.register(city)
class cityAdmin(ImportExportModelAdmin):
    pass
        
@admin.register(income)
class incomeAdmin(ImportExportModelAdmin):
    pass


@admin.register(Qualification)
class QualificationAdmin(ImportExportModelAdmin):
    pass


@admin.register(work)
class workAdmin(ImportExportModelAdmin):
    pass


@admin.register(experience)
class experienceAdmin(ImportExportModelAdmin):
    pass


@admin.register(hobbies)
class hobbiesAdmin(ImportExportModelAdmin):
    pass


@admin.register(medical_condition)
class medical_conditionAdmin(ImportExportModelAdmin):
    pass

