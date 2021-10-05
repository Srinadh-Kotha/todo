from django.contrib import admin

from pyNKSapp.models import signupdetails,enrolled,staff_details,todo_list,trash
# Register your models here.

admin.site.register(signupdetails)
admin.site.register(enrolled)
admin.site.register(staff_details)
admin.site.register(todo_list)
admin.site.register(trash)