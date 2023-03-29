from django.contrib import admin
from Employee_data.models import EmployeeData,EmployeeSalary,Expenses,SalaryPDFFiles
# Register your models here.
admin.site.register(EmployeeData)
admin.site.register(EmployeeSalary)
admin.site.register(Expenses)
admin.site.register(SalaryPDFFiles)


class Meta:
    model = EmployeeData,EmployeeSalary,Expenses,SalaryPDFFiles
