from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MessageThread, CaseMessage

@login_required
def thread_list(request):
    threads = request.user.message_threads.filter(is_deleted=False).select_related('case')
    return render(request, 'communications/thread_list.html', {'threads': threads})

@login_required
def thread_detail(request, pk):
    thread = get_object_or_404(MessageThread, pk=pk)
    messages = thread.messages.all().select_related('sender').order_by('created_at')
    return render(request, 'communications/thread_detail.html', {'thread': thread, 'messages': messages})
