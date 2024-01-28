from django.contrib import admin
from app1.models import profile,family_details,media,gallery,document,follow

admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Panel Portal"
admin.site.index_title = "Welcome to Admin Panel Portal"

# Register your models here.
# admin.site.register(profile)

admin.site.register(family_details)
admin.site.register(media)
admin.site.register(gallery)
admin.site.register(document)





class profileAdmin(admin.ModelAdmin):
    list_display = ('user','user_id','mobile','marrital_status','is_featured','is_approved','is_mail_verified')
    list_editable = ('is_featured','is_approved','is_mail_verified',)
    list_filter=['related_officer','is_approved']
admin.site.register(profile, profileAdmin)


class followAdmin(admin.ModelAdmin):
    list_display = ('ufrom','uto','status')
    
admin.site.register(follow, followAdmin)
