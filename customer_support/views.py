from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from customers.models import ServiceRequest
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now 

def manage_requests(request):
    requests = ServiceRequest.objects.all().order_by('status', 'submitted_at')
    return render(request, 'manage_requests.html', {'requests': requests})

@login_required
def view_request(request, request_id):
    if not request.user.groups.filter(name="Support").exists():
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    return render(request, 'view_request.html', {'service_request': service_request})

@login_required
# def resolve_request(request, request_id):
#     if not request.user.groups.filter(name="Support").exists():
#         return HttpResponseForbidden("You do not have permission to access this page.")
    
#     service_request = get_object_or_404(ServiceRequest, id=request_id)
#     if service_request.status != 'resolved':
#         service_request.resolve()
#     return redirect('manage_requests')
def resolve_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    service_request.status = 'resolved'
    service_request.resolved_at = now()  
    service_request.save()  
    return redirect('support:manage_requests')

