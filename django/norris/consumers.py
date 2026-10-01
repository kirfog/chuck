import asyncio

from channels.generic.websocket import AsyncWebsocketConsumer


class joke_consumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        asyncio.create_task(self.channel_layer.group_add("group1", self.channel_name))

    async def disconnect(self, close_code):
        asyncio.create_task(
            self.channel_layer.group_discard("group1", self.channel_name)
        )

    async def send_joke(self, event):
        await self.send(event["text"])
