from django.contrib import admin
from app1.models import profile,family_details,media,gallery,document,follow,user_level,reginal_manager_profile

admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Panel Portal"
admin.site.index_title = "Welcome to Admin Panel Portal"

# Register your models here.
# admin.site.register(profile)

admin.site.register(family_details)
admin.site.register(media)
admin.site.register(gallery)
admin.site.register(document)
admin.site.register(reginal_manager_profile)




class user_levelAdmin(admin.ModelAdmin):
    list_display = ('user','access_type','reginal_manager')
    list_editable = ('access_type','reginal_manager',)
    list_filter=['access_type',]
admin.site.register(user_level, user_levelAdmin)



class profileAdmin(admin.ModelAdmin):
    list_display = ('user','user_id','mobile','marrital_status','is_featured','is_approved','is_mail_verified')
    list_editable = ('is_featured','is_approved','is_mail_verified',)
    list_filter=['related_officer','is_approved']
admin.site.register(profile, profileAdmin)


class followAdmin(admin.ModelAdmin):
    list_display = ('ufrom','uto','status')
    
admin.site.register(follow, followAdmin)




