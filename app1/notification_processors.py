# context_processors.py
from app1.models import follow

def follow_requestfrom(request):
    follow_requests = []
    if request.user.is_authenticated:
        # Get all follow instances with uto as the current user and status as 'Requested'
        follow_requests = follow.objects.filter(uto=request.user, status='Requested')
    return {'follow_requests': follow_requests}
