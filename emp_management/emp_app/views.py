from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Employee, Appointment, Department
from .forms import EmployeeForm
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request, "home.html")


def emp_list(request):
    employees=Employee.objects.all()
    return render(request, 'emp_list.html', {'employees': employees})


def emp_add(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('emp_list')
    else:
        form = EmployeeForm()
    return render(request, 'emp_add.html', {'form':form})


def emp_delete(request, id=0):
    if id:
        try:
            employees = Employee.objects.get(pk=id)
            employees.delete()
            messages = "Employee remove successfully"
            return redirect('emp_list')
        except:
            messages = "Your giving information invalid"
    
    employees = Employee.objects.all()
    return render(request, 'emp_delete.html', {'employees': employees})


def emp_edit(request, id):
    employees = Employee.objects.get(pk = id)
    form = EmployeeForm(instance = employees)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance = employees )        
        if form.is_valid():
           form.save()                 
           return redirect('emp_list')        
    return render(request, 'emp_add.html', {'form':form})

def emp_filter(request):
    if request.method =='POST':
        name = request.POST['name']
        department = request.POST['department']
        designation = request.POST['designation']
        employees = Employee.objects.all()
        if name:
            employees = employees.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
               
        if department:
            employees = employees.filter(department__name__icontains = department)
        if designation:
            employees = employees.filter(designation__name__icontains = designation)
        return render(request, 'emp_list.html', {'employees':employees})
    else:
        return render(request, 'emp_filter.html')
    
# def searchitem(request):
#     if request.method == 'GET':
#         query = request.GET.get('si')
#         if query:
#             employees = Employee.objects.filter(first_name__icontains = query)
#             # employees = Employee.objects.filter(last_name__icontains = query)
#             # employees = Employee.objects.filter(department__name__icontains = query)
#             # employees = Employee.objects.filter(email__icontains = query)
#             # employees = Employee.objects.filter(designation__name__icontains = query)
#             # employees = Employee.objects.filter(phone__icontains = query)
#             return render(request, 'emp_list.html', {'employees':employees})
#         else:
#             return HttpResponse('Invalid search item')
#     else:
#         return render(request, 'emp_list.html', {})
            

def userLogin(request):
    pass


def userRegistration(request):
    pass

            
    
    



   
        
            
            
            
        
                
   