
from django.contrib import admin

from TokenAuthentication_App.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','salary','email']
    search_fields = ['ename']
    list_display_links = ['email']
    readonly_fields = ['eno']
    list_editable = ['salary']
    exclude = ['email']
    list_filter = ['ename']

admin.site.register(Employee,EmployeeAdmin)