from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import Group
from django.contrib import messages
from .models import Customer
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect based on group
            if user.groups.filter(name='Support').exists():
                return redirect('support:manage_requests')  # Update with actual support dashboard URL
            else:
                return redirect('/customer/track/')  # Update with actual customer dashboard URL
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Assign to the "Customer" group (if applicable)
            group, created = Group.objects.get_or_create(name="Customer")
            user.groups.add(group)
            
            # Create a Customer instance for this user
            phone = request.POST.get('phone', '')
            address = request.POST.get('address', '')
            Customer.objects.create(user=user, phone=phone, address=address)
            
            return redirect('/customer/track/')  # Redirect to tracking page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
def create_request(request):
    try:
        customer = request.user.customer  # Access the related Customer instance
    except Customer.DoesNotExist:
        return HttpResponseForbidden("You are not registered as a customer.")
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            return redirect('/customer/track/')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_request.html', {'form': form})

# def track_request(request):
#     requests = ServiceRequest.objects.filter(customer=request.user.customer)
#     return render(request, 'request_status.html', {'requests': requests})
def track_request(request):
    try:
        customer = request.user.customer  # Access the related Customer instance
    except Customer.DoesNotExist:
        return HttpResponseForbidden("You are not registered as a customer.")
    
    # Fetch the requests for this customer
    requests = ServiceRequest.objects.filter(customer=customer)
    return render(request, 'request_status.html', {'requests': requests})
