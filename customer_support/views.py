from django.shortcuts import render
from customers.models import ServiceRequest

def manage_requests(request):
    requests = ServiceRequest.objects.all().order_by('status', 'submitted_at')
    return render(request, 'manage_requests.html', {'requests': requests})
