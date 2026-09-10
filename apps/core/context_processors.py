from django.conf import settings

def civiclaw_context(request):
    return {
        'PLATFORM_NAME': getattr(settings, 'CIVICLAW_PLATFORM_NAME', 'CivicLaw Enterprise'),
        'PLATFORM_TAGLINE': getattr(settings, 'CIVICLAW_PLATFORM_TAGLINE', 'AI-Powered Legal Suite'),
        'PLATFORM_VERSION': getattr(settings, 'CIVICLAW_VERSION', '2.4.0'),
        'current_user_role': getattr(request.user, 'role', 'GUEST') if request.user.is_authenticated else 'ANONYMOUS',
    }
