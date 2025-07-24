from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message

# Create your views here.

@login_required
def chat_view(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            Message.objects.create(user=request.user, text=text)
            return redirect('chat:chat')
    messages = Message.objects.filter(user=request.user).order_by('timestamp')
    return render(request, 'chat/chat.html', {'messages': messages})
