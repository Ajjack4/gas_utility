from django.shortcuts import render, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def create_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user.customer
            service_request.save()
            return redirect('track_request')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_request.html', {'form': form})

def track_request(request):
    requests = ServiceRequest.objects.filter(customer=request.user.customer)
    return render(request, 'request_status.html', {'requests': requests})
