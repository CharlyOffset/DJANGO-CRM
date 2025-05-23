from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

def home(request):
    records = Record.objects.all()


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('hellloooo')
            messages.success(request, "You have logged in Successfully")
            return redirect('home')
        else:
            print('hellloooo2222')
            messages.success(request, "There was an error login in please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
      if request.user.is_authenticated:
            # look up Records
            customer_record = Record.objects.get(id=pk)
            return render(request, 'record.html', {'customer_record':customer_record})
      else:
            messages.success(request, "You Must Be Logged in To View This Page!")
            return redirect('home')
      
def delete_record(request, pk):
      if request.user.is_authenticated:
            delete_it = Record.objects.get(id=pk)
            delete_it.delete()
            messages.success(request, "You have deleted This Record Successfully")
            return redirect('home')
      else:
           messages.success(request, "You Must Be Logged In To delete This Record")
           return redirect('home') 
      
def add_record(request):
      form = AddRecordForm(request.POST or None)
      if request.user.is_authenticated:
            if request.method == "POST":
                  if form.is_valid():
                        add_record = form.save()
                        messages.success(request, "Record Added...")
                        return redirect('home')
            return render(request, 'add_record.html', {'form': form})
      else:
            messages.success(request, "You Must Be Logged in")
            return redirect('home')
      
def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')