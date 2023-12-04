from channels.consumer import SyncConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User
from chat.models import Thread, Message
from channels.exceptions import StopConsumer
import json


class ChatConsumer(SyncConsumer):
    http_user = True
    def websocket_connect(self, event):
        me = self.scope['user']
        
        other_username = self.scope['url_route']['kwargs']['username']
        other_user = User.objects.get(username=other_username)
        self.thread_obj = Thread.objects.get_or_create_personal_thread(me, other_user)
        self.room_name = f'presonal_thread_{self.thread_obj.id}'
        async_to_sync(self.channel_layer.group_add)(self.room_name, self.channel_name)
        self.send({
            'type': 'websocket.accept'
        })
        print(f'[{self.channel_name}] - You are connected')

    def websocket_receive(self, event):
        print(f'[{self.channel_name}] - Recieved message - {event["text"]}')

        msg = json.dumps({
            'text': event.get('text'),
            'username': self.scope['user'].username
        })

        self.store_message(event.get('text'))

        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
             {
                'type': 'websocket.message',
                'text': msg
             }
        )

    def websocket_message(self, event):
        print(f'[{self.channel_name}] - Message sent - {event["text"]}')
        self.send({
            'type': 'websocket.send',
            'text': event.get('text')
        })

    def websocket_disconnect(self, event):
        print(f'[{self.channel_name}] - Disonnected')
        async_to_sync(self.channel_layer.group_discard)(self.room_name, self.channel_name)
        
        raise StopConsumer()

    def store_message(self, text):
        Message.objects.create(
            thread = self.thread_obj,
            sender = self.scope['user'],
            text = text
        )

