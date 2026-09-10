from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def status_badge(status):
    badge_map = {
        'DRAFT': 'badge-secondary',
        'INTAKE': 'badge-info',
        'ACTIVE': 'badge-primary',
        'HEARING_SCHEDULED': 'badge-warning',
        'JUDGMENT_RESERVED': 'badge-dark',
        'DISPOSED': 'badge-success',
        'CLOSED': 'badge-secondary',
        'PAID': 'badge-success',
        'OVERDUE': 'badge-danger',
        'PENDING': 'badge-warning',
    }
    cls = badge_map.get(str(status).upper(), 'badge-light')
    return mark_safe(f'<span class="badge {cls}">{status}</span>')

@register.filter
def priority_badge(priority):
    p_map = {
        'CRITICAL': 'badge-danger',
        'HIGH': 'badge-warning',
        'MEDIUM': 'badge-info',
        'LOW': 'badge-secondary',
    }
    cls = p_map.get(str(priority).upper(), 'badge-light')
    return mark_safe(f'<span class="badge {cls}">{priority}</span>')
