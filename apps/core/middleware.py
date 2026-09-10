import time
import uuid
from django.utils.deprecation import MiddlewareMixin

class AuditMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.request_id = str(uuid.uuid4())
        request.start_time = time.time()
        
    def process_response(self, request, response):
        duration = time.time() - getattr(request, 'start_time', time.time())
        response['X-Request-ID'] = getattr(request, 'request_id', 'unknown')
        response['X-Response-Time-Ms'] = str(round(duration * 1000, 2))
        return response

class TenantContextMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            request.firm = getattr(request.user, 'law_firm', None)
        else:
            request.firm = None
