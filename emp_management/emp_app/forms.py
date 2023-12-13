from django import forms
from .models import Employee, Department, Appointment


class EmployeeForm(forms.ModelForm):
    # hiring_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))    
    class Meta:
        model = Employee
        fields = ['first_name','last_name', 'department', 'designation', 'salary', 'bonus', 'phone','email', 'hiring_date']        
        widgets = {
            'first_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'department' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Department'}),
            'designation' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Designation'}),
            'salary' : forms.NumberInput(attrs={'class':'form-control'}),
            'bonus' : forms.NumberInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Example@gmail.com'}),
            'hiring_date' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
        }
        
        