from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.http import JsonResponse
from django.core import serializers
import json
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

def index(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            login(request, user)
            return redirect('/student_list')
    return render(request, 'home.html')


def user_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(username=username,password=make_password(password))
        if user:
            return redirect('/user_login')   
    return render(request, 'user_registration.html')


@login_required(login_url="/user_login")
def create_marksheet(request):
    if request.method == 'POST':
            form = StudentForm(request.POST, request.FILES)  
            if form.is_valid():
                form.save()  
                return redirect('/student_list')
            else:
                errors = {}
                for field, field_errors in form.errors.items():
                    error_messages = []
                    for error in field_errors:
                        error_messages.append(error)
                errors[field] = error_messages
                messages.error(request, errors)
                
    form = StudentForm()
    return render(request, 'index.html', {'form': form})

@login_required(login_url="/user_login")
def student_list(request):
    return render(request,'student_list.html')

@login_required(login_url="/user_login")
def student_data(request):
    student_data = Student.objects.all()
    serialized_data = serializers.serialize('json', student_data)
    data_dict = json.loads(serialized_data)
    data_list = []
    for data in data_dict:
        data_list.append(data['fields'])
        
    return JsonResponse({'data': data_list}, safe=False)
    