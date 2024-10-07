from django.shortcuts import render, redirect
from .models import Company, Employee
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.
def employee_registration(request):
    template_name = 'employee/employee-registration.html'
    context = {'companies': Company.objects.all()}

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        employee_name = request.POST.get('employee_name')
        designation = request.POST.get('designation')
        shift = request.POST.get('shift')
        company_id = request.POST.get('company')

        if not (username and email and password and employee_name and designation and shift and company_id):
            messages.error(request, 'All fields are required.')
            return render(request, template_name, context)
        
        try:
            with transaction.atomic():
                user = User.objects.create_user(username=username, email=email, password=password)
                company = Company.objects.get(id=company_id)

                employee = Employee.objects.create(
                    user=user,
                    employee_name=employee_name,
                    designation=designation,
                    shift=shift,
                    company_id=company
                )

                messages.success(request, 'Employee details added successfully.')
                return redirect('success_page')

        except Company.DoesNotExist:
            messages.error(request, 'Selected company does not exist.')
            return render(request, template_name, context)
        
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return render(request, template_name, context)
        
    return render(request, template_name, context)

def success_page(request):
    template_name = 'employee/successfull.html'
    return render(request, template_name)

def error_page(request):
    template_name = 'employee/error.html'
    context = {'error_message': 'An unexpected error occurred.'}
    return render(request, template_name, context)

def profile(request, user_id):
    template_name = ''
    context = {}
    try:
        employee = Employee.objects.get(user_id=user_id)
        context = {"employee": employee}
        template_name = 'employee/profile.html'

        return render(request, template_name, context)
    
    except Employee.DoesNotExist:
        template_name = 'employee/error.html'
        context = {'error_message': 'Employee not found!'}
        
        return render(request, template_name, context)

        

def login_view(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            
            try:
                return redirect('profile', user_id=user.id)
            
            except Employee.DoesNotExist:
                messages.error(request, 'Employee profile not found.')
                return redirect('login')
            
        else:
            messages.error(request, 'Invalid username or password!')

    template_name = 'employee/login.html'
    context = {}
    return render(request, template_name, context)

def company_registration(request):
    if request.method == 'POST':
        company_id = request.POST.get('company_id')
        company_name = request.POST.get('company_name')
        company_building_name = request.POST.get('company_building_name')
        company_floor = request.POST.get('company_floor')
        company_parking_place_number = request.POST.get('company_parking_place_number')

        if not (company_id and company_name and company_building_name and company_floor and company_parking_place_number):
            messages.error(request, 'All fields are required!')
        else:
            try:
                # Create and save the new company
                Company.objects.create(
                    id=company_id,
                    company_name=company_name,
                    company_building_name=company_building_name,
                    company_floor=company_floor,
                    company_parking_place_number=company_parking_place_number
                )
                messages.success(request, 'Company registered successfully!')
                return redirect('company_registration')
            except Exception as e:
                messages.error(request, f"Error: {str(e)}")

    companies = Company.objects.all()
    template_name = 'employee/company-registration.html'
    context = {'companies': companies}
    return render(request, template_name, context)


def home_page(request):
    template_name = 'Home.html'
    context = {}

    return render(request, template_name, context)