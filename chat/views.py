from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import get_user_model
from django.shortcuts import Http404
from chat.models import Thread, Message


class ThreadView(View):
    template_name = 'chat/chat-home.html'

    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)

    def get_object(self):
        other_username  = self.kwargs.get("username")
        self.other_user = get_user_model().objects.get(username=other_username)
        obj = Thread.objects.get_or_create_personal_thread(self.request.user, self.other_user)
        if obj == None:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        context = {}
        context['me'] = self.request.user
        context['thread'] = self.get_object()
        context['user'] = self.other_user
        context['messages'] = self.get_object().message_set.all()
        return context

    def get(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context=context)

    def post(self, request, **kwargs):
        self.object = self.get_object()
        thread = self.get_object()
        data = request.POST
        user = request.user
        text = data.get("message")
        Message.objects.create(sender=user, thread=thread, text=text)
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context=context)
    
    



# def chat2(request,receiver):
#     receiver=receiver
#     reciverobj = User.objects.get(id=receiver)
    
#     msgobj=Message.objects.filter(receiver_id=receiver,sender_id=request.user.id)
#     msgobjleft=Message.objects.filter(receiver_id=request.user.id,sender_id=receiver)
    
    
#     if request.method == 'POST':
#         msg = request.POST.get('msg')
#         obj=Message(sender_id=request.user.id,receiver_id=receiver,msg=msg)
#         obj.save()
        
#     data={
#         'reciverobj':reciverobj,
#         'msgobj':msgobj,
#         'msgobjleft':msgobjleft
#     }
#     return render(request,"chat/chat-home2.html",data)