from django.contrib import admin
from chat.models import Message

admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Panel Portal"
admin.site.index_title = "Welcome to Admin Panel Portal"


admin.site.register(Message)
