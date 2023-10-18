from django.contrib import admin
from app1.models import profile,family_details,media

admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Panel Portal"
admin.site.index_title = "Welcome to Admin Panel Portal"

# Register your models here.
# admin.site.register(profile)

admin.site.register(family_details)
admin.site.register(media)


class profileAdmin(admin.ModelAdmin):
    list_display = ('user','mobile','marrital_status','is_featured','is_verified')
    list_editable = ('marrital_status','is_featured','is_verified',)

admin.site.register(profile, profileAdmin)