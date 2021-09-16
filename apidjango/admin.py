from django.contrib import admin
from apidjango.models import Employee


# @admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department')
    list_display_links = ('name',)


admin.site.register(Employee, EmployeesAdmin)
