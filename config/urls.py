from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='accounts:dashboard_redirect', permanent=False), name='root_redirect'),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('firms/', include('apps.firms.urls', namespace='firms')),
    path('clients/', include('apps.clients.urls', namespace='clients')),
    path('courts/', include('apps.courts.urls', namespace='courts')),
    path('cases/', include('apps.cases.urls', namespace='cases')),
    path('hearings/', include('apps.hearings.urls', namespace='hearings')),
    path('documents/', include('apps.documents.urls', namespace='documents')),
    path('evidence/', include('apps.evidence.urls', namespace='evidence')),
    path('research/', include('apps.legal_research.urls', namespace='legal_research')),
    path('tasks/', include('apps.tasks.urls', namespace='tasks')),
    path('deadlines/', include('apps.deadlines.urls', namespace='deadlines')),
    path('communications/', include('apps.communications.urls', namespace='communications')),
    path('billing/', include('apps.billing.urls', namespace='billing')),
    path('orders/', include('apps.orders_judgments.urls', namespace='orders_judgments')),
    path('notifications/', include('apps.notifications.urls', namespace='notifications')),
    path('analytics/', include('apps.analytics.urls', namespace='analytics')),
    path('audit/', include('apps.audit.urls', namespace='audit')),
    path('ai/', include('apps.ai_engine.urls', namespace='ai_engine')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
