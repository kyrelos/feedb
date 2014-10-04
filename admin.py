from django.contrib import admin
from feedb.models import*

# Register your models here.

class CustomerInline(admin.TabularInline):
    model=Customer
    extra=0


class CompanyAdmin(admin.ModelAdmin):
##    list_display=('name', 'description')
    inlines=[CustomerInline, ]
    search_fields=['name']
    

class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name', 'phone_number', 'company')
    list_filter=('company',)

class EmployeeAdmin(admin.ModelAdmin):
    search_fields=['first_name','last_name']

    

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Company,CompanyAdmin)
