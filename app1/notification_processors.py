# context_processors.py
from app1.models import follow
from chat.models import Message

def follow_requestfrom(request):
    follow_requests = []
    if request.user.is_authenticated:
        # Get all follow instances with uto as the current user and status as 'Requested'
        follow_requests = follow.objects.filter(uto=request.user, status='Requested')
    return {'follow_requests': follow_requests}



def unread_messages_count(request):
    if request.user.is_authenticated:
        unread_count = Message.objects.filter(thread__users=request.user, is_read=False).count()
    else:
        unread_count = 0

    return {'unread_messages_count': unread_count}
