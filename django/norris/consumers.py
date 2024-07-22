from channels.generic.websocket import AsyncWebsocketConsumer

class joke_consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('group1', self.channel_name)
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard('group1', self.channel_name)
    
    async def send_joke(self, event):
        await self.send(event['text'])

