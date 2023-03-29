import datetime

from django.db import models
# Create your models here.


class EmployeeData(models.Model):
    Employee_ID = models.IntegerField(unique=True)
    Employee_FirstName = models.CharField(max_length=100)
    Employee_MiddleName = models.CharField(max_length=100)
    Employee_LastName = models.CharField(max_length=100)
    Employee_EmailID = models.EmailField()
    Employee_Date_of_joined = models.DateField()
    Employee_Department = models.CharField(max_length=64,null=True)
    Employee_Sub_Department = models.CharField(max_length=64,default='',null=True)
    Employee_Designation = models.CharField(max_length=64,null=True)
    Employee_CTC = models.FloatField(null=True)
    Employee_Salary = models.FloatField(null=True)
    Employee_Bank_Name = models.CharField(max_length=64,default='',null=True)
    Employee_Bank_Account_Number = models.IntegerField(default='',null=True)
    Employee_Bank_IFSC_Code = models.CharField(max_length=64,default='',null=True)
    Employee_Pan_Number = models.CharField(max_length=64,default='',null=True)
    Employee_UAN_Number = models.IntegerField(default='',null=True)
    Employee_PF_Number = models.CharField(max_length=64,default='',null=True)
    Employee_ESI_Number = models.IntegerField(default='',null=True)
    Employee_Profile_Photo = models.ImageField(upload_to="Employee_Photo",default='',null=True)
    Employee_Signature_Photo = models.ImageField(upload_to="Employee_Sign", default='', null=True)
    Employee_Paid_leaves = models.IntegerField(null=True)

    def __str__(self):
        return self.Employee_FirstName


class EmployeeSalary(models.Model):
    Employee_ID = models.IntegerField(unique=True)
    Employee_FirstName = models.CharField(max_length=100)
    Employee_MiddleName = models.CharField(max_length=100)
    Employee_LastName = models.CharField(max_length=100)
    Employee_Department = models.CharField(max_length=64)
    Employee_Designation = models.CharField(max_length=64)
    Employee_Date_of_joined = models.DateField()
    Employee_Bank_Name = models.CharField(max_length=64,null=True)
    Employee_Bank_Account_Number = models.IntegerField(null=True)
    Employe_Bank_IFSC_Code = models.CharField(max_length=64,null=True)
    Employee_Pan_Number = models.CharField(max_length=64,null=True)
    Employee_UAN_Number = models.IntegerField(default=True)
    Employee_PF_Number = models.CharField(max_length=64,null=True)
    Employee_ESI_Number = models.IntegerField(null=True)
    Employee_Salary = models.FloatField(null=True)
    Employee_Actual_Payable_Days = models.FloatField(null=True)
    Employee_Total_Working_Days = models.FloatField(null=True)
    Employee_Loss_Of_Pay_Days = models.FloatField(default=True)
    Employee_Paid_Leaves = models.FloatField()
    Employee_Basic = models.FloatField()
    Employee_Conveyance_Allowance = models.FloatField()
    Employee_HRA = models.FloatField()
    Employee_Medical_Allowance = models.FloatField()
    Employee_Special_Allowance = models.FloatField()
    Employee_Variable_Pay = models.FloatField()
    Employee_Total_Earnings = models.FloatField()
    Employee_PF_Employee = models.FloatField()
    Employee_PF_Employer = models.FloatField()
    Employee_ESI_Employee = models.FloatField(null=True)
    Employee_ESI_Employer = models.FloatField()
    Employee_Total_Contributions = models.FloatField()
    Employee_Professional_Tax = models.FloatField()
    Employee_Total_Deductions = models.FloatField()
    Employee_Net_Salary = models.FloatField()
    Employee_Salary_Month_and_Year = models.DateField(auto_now=True)

    def __str__(self):
        return self.Employee_FirstName

class Expenses(models.Model):
    SrNo = models.IntegerField(primary_key=True,auto_created=True)
    Date= models.DateField()
    billNo =models.CharField(max_length=64)
    price = models.FloatField()
    bill_image = models.ImageField(upload_to="Expenses",default='',null=True)

    def __str__(self):
        return self.billNo

class SalaryPDFFiles(models.Model):
    Employee_Id = models.CharField(max_length=64)
    Employee_Firstname = models.CharField(max_length=64,default='')
    Employee_Lastname = models.CharField(max_length=64,default='')
    Employee_SalaryPDFFiles = models.FileField(upload_to='')

    def __str__(self):
        return self.Employee_Firstname
