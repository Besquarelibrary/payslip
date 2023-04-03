from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import EmployeeData,Expenses,SalaryPDFFiles
import datetime
import win32com.client
import os
# from .forms import Expensesdataupload
from django.views import View
import openpyxl
import win32com.client
import pythoncom
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from num2words import num2words
# Create your views here.
def home(request):
    return render(request, "welcome.html")
def employeeDetails(request):
    empdetails = EmployeeData.objects.all()
    return render(request, 'Employee_details.html', {"empdetails":empdetails})

class getEmployeeById(View):
    def get(self,request):
        return render(request,'getemployeedetails.html')
    def post(self,request):
        try:
            id = request.POST['eid']
            employeeRecord = EmployeeData.objects.get(Employee_ID=id)
            print(employeeRecord.Employee_Date_of_joined)
            Dateofjoined = employeeRecord.Employee_Date_of_joined.strftime('%m-%d-%Y')
            date = datetime.datetime.now() - datetime.timedelta(days=26)
            month = date.month
            month_number = "%d" % month
            l=[['1','3','5','7','8','10','12'],['2'],['4','6','9','11']]
            if month_number in l[0]:
                actualdays = 31
            elif month_number in l[1]:
                actualdays = 28
            elif month_number in l[2]:
                actualdays = 30
            return render(request,'empsal.html',{'employeeRecord':employeeRecord,'dateofjoined':Dateofjoined,'actualdays':actualdays})
        except EmployeeData.DoesNotExist:
            return render(request,'getemployeedetails.html',{'msg':'does not exist'})

def Salary(request):
    id=request.POST["EmpID"]
    firstname=request.POST["EmpFirstname"]
    middlename = request.POST["EmpMiddlename"]
    lastname = request.POST["EmpLastname"]
    department = request.POST["EmpDepartment"]
    designation = request.POST["EmpDesignation"]
    dateofjoined = request.POST["EmpDateofjoined"]
    bankname= request.POST["EmpBankname"]
    accountnumber = request.POST["EmpBankaccountnumber"]
    ifsccode = request.POST["EmpIfsccode"]
    pannumber = request.POST["EmpPannumber"]
    uannumber = request.POST["EmpUannumber"]
    pfnumber = request.POST["EmpPfnumber"]
    esinumber =request.POST["EmpEsinumber"]
    actualworkingdays = request.POST["EmpActualworkingdays"]
    totalworkingdays = request.POST["EmpTotalworkingdays"]
    lossofdays = request.POST["EmpLossofpaydays"]
    paidleaves = request.POST["EmpPaidleaves"]
    dayspayable= request.POST["EmpDayspayable"]
    basic = request.POST["EmpBasic"]
    coveyanceallowance = request.POST["EmpConveyanceallowance"]
    hra = request.POST["EmpHra"]
    medicalallowance = request.POST["EmpMedicalallowance"]
    specialallowance=request.POST["EmpSpecialallowance"]
    variablepay = request.POST["EmpVariablepay"]
    totalearnings = request.POST["EmpTotalearnings"]
    pfemployee= request.POST["EmpPfemployee"]
    pfemployer = request.POST["EmpPfemployer"]
    esiemployee =request.POST["EmpEsiemployee"]
    esiemployer = request.POST["EmpEsiemployer"]
    totalcontributions=request.POST["EmpTotalcontributions"]
    professionaltax=request.POST["EmpProfessionaltax"]
    totaldeductions =request.POST["EmpTotaldeductions"]
    netpayable = request.POST["EmpNetpayable"]
    file='myfile.xlsx'
    folder='Employee_data\static\excel'
    path = os.path.join(os.getcwd(),folder,file)
    print(path)
    # path = "F:\\payment\\Payment_system\\Employee_data\\static\\excel\\myfile.xlsx"
    ref_workbook = openpyxl.load_workbook(path)
    date = datetime.datetime.now() - datetime.timedelta(days=26)
    print(date)
    month = date.month
    month_number = "%d" % month
    datetime_object = datetime.datetime.strptime(month_number, "%m")
    month_name = datetime_object.strftime("%b")
    print(month_name)
    year = date.year
    wb=ref_workbook.get_sheet_names()
    sheet=ref_workbook.get_sheet_by_name('Sheet1')
    sheet["A1"] = "PAYSLIP %s %d" % (month_name,year)
    sheet["A8"] = "%s %s %s" %(firstname,middlename,lastname)
    sheet["A11"] =id
    sheet["C11"]=dateofjoined
    sheet["E11"]=department
    sheet["G11"]="-"
    sheet["A14"]=designation
    sheet["C14"]="Bank Transfer"
    sheet["E14"]=bankname
    sheet["G14"]=ifsccode
    sheet["A17"]=accountnumber
    sheet["C17"]=pannumber
    sheet["E17"]=uannumber
    sheet["G17"]=pfnumber
    sheet["A20"]=esinumber
    sheet["A26"]=actualworkingdays
    sheet["C26"]=totalworkingdays
    sheet['E26']=lossofdays
    sheet["G26"]=dayspayable
    sheet["C29"]=basic
    sheet["C30"]=coveyanceallowance
    sheet["c31"]=hra
    sheet["c32"]=medicalallowance
    sheet["C33"]=specialallowance
    sheet["C34"]=variablepay
    sheet["C35"]=totalearnings
    sheet["G29"]=pfemployee
    sheet["G30"]=pfemployer
    sheet["G31"]=esiemployee
    sheet["G32"]=esiemployer
    sheet["G33"]=totalcontributions
    sheet["G37"]=professionaltax
    sheet["G38"]=totaldeductions
    sheet["C40"]=netpayable
    a=sheet["C41"]=num2words(netpayable)+' only'
    print(a)
    file = ("%s %s-Payslip-%s-%d.xlsx" %(firstname,lastname,month_name,year))
    folder_path = 'payslip'
    # ref_workbook.save(f"F:\\payment\\Payment_system\\payslip\\{file}")
    file_path = os.path.join(folder_path, file)
    ref_workbook.save(file_path)
    return render(request,"getemployeedetails.html")


class ExpensesCompany(View):
    def get(self,request,*args,**kwargs):
        # context = {'form':Expensesdataupload()}
        return render(request,'addexpenses.html')
    def post(self,request, *args, **kwargs):
        if request.method == 'POST' and request.FILES:
            bill_number = request.POST["billnumber"]
            bill_price = request.POST["billprice"]
            bill_date = request.POST["billdate"]
            billimage = request.FILES["image"]
            Expenses_record = Expenses(billNo=bill_number, price=bill_price, Date=bill_date, bill_image=billimage)
            Expenses_record.save()
        # print('POST Method Called : ', request.FILES)
        # form = Expensesdataupload(request.POST, request.FILES)
        # print("Is Form Valid : ", form.is_valid())
        # if form.is_valid():
        #     book = form.save()
        #     book.save()
            status = {'status':'Expense Details Saved Successfully'}

            return render(request,'status.html',status)
        


def allExpensesDetails(request):
    allexpensedetails = Expenses.objects.all()
    return render(request,'GetExpensesdetails.html',{'allexpensesdetails':allexpensedetails})

def get_files_in_folder(folder_path):
    files = []
    for file_name in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file_name)):
            files.append(file_name)
    return files


def get_files_in_folder_pdf(folder_path_pdf):
    files_pdf = []
    for file_name in os.listdir(folder_path_pdf):
        if os.path.isfile(os.path.join(folder_path_pdf, file_name)):
            files_pdf.append(file_name)
    return files_pdf


class my_view(View):
    def get(self, request):
        folder_path = 'payslip'
        files = get_files_in_folder(folder_path)
        print(files)
        for file in files:
            WB_PATH = os.path.join(os.getcwd(),folder_path,file)
            print(WB_PATH)
            file_pdf = file.split('.')
            print(file_pdf)
            folder = 'pdf salary'
            path = os.path.join(os.getcwd(),folder,file_pdf[0])
            PATH_TO_PDF = f'{path}.pdf'
            excel = win32com.client.Dispatch("Excel.Application", pythoncom.CoInitialize())
            excel.Visible = False
            try:
                print('Start conversion to PDF')
                Workbooks = excel.Workbooks.Open(WB_PATH)
                Workbooks.ActiveSheet.ExportAsFixedFormat(0, PATH_TO_PDF)
                Workbooks.Close(False)
                excel.Quit()
            # finally:
            #     print('Succeeded.')
            #     os.remove(WB_PATH)


# def salaryslipsent(request):
        folder_path_pdf = 'pdf salary'
        files_pdf = get_files_in_folder_pdf(folder_path_pdf)
        print(files_pdf)
        for file_pdf in files_pdf:
            print(type(file_pdf))
            attachment = file_pdf
            print(attachment)
            users = EmployeeData.objects.all()
            for user in users:
                fname = user.Employee_FirstName
                lname =user.Employee_LastName
                print(fname)
                print(lname)
                if (fname and lname) in attachment:
                    date = datetime.datetime.now() - datetime.timedelta(days=20)
                    month = date.month
                    month_number = "%d" % month
                    datetime_object = datetime.datetime.strptime(month_number, "%m")
                    month_name = datetime_object.strftime("%b")
                    print(month_name)
                    year = date.year
                    subject = 'Salary Slip'
                    message = f'Besquare Technologies please check Your Salary slip {month_name} month and {year} year,If you Have any queries you can contact immediately conatct HR.'
                    recipient_list = user.Employee_EmailID
                    print(recipient_list)

                    email = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [recipient_list])
                    print(email)
                    print(attachment)
                    folder_name = 'pdf salary'
                    file_name = attachment
                    file_path = os.path.join(os.getcwd(),folder_name,file_name)

                    print(file_path)

                    if os.path.exists(file_path):
                        with open(file_path, 'rb') as f:

                            email.attach(file_name, f.read(), 'application/pdf')
                            email.send()
                            # Salaries = SalaryPDFFiles(Employee_Id=user.id,Employee_SalaryPDFFiles=file_name)
                            # Salaries.save()
                            print('email sent')

        return render(request, 'status.html')



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def Email(request):
    from_addr = 'info@besquaretech.com'
    to_addr = 'hnaitanwar@gmail.com'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Today'
    msg["To"] =(to_addr)
    s= smtplib.SMTP('mail.besquaretech.com', 465)
    try:
        s.sendmail(from_addr, [to_addr],msg.as_string())
    except Exception as e:
        print(e)

    return render(request, 'status.html')
