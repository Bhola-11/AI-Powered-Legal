from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CourtOrder, ComplianceItem

@login_required
def order_list(request):
    orders = CourtOrder.objects.filter(is_deleted=False).select_related('case', 'presiding_judge').order_by('-order_date')
    return render(request, 'orders/order_list.html', {'orders': orders})

@login_required
def order_detail(request, pk):
    order = get_object_or_404(CourtOrder, pk=pk)
    compliance_items = order.compliance_items.all()
    return render(request, 'orders/order_detail.html', {'order': order, 'compliance_items': compliance_items})
