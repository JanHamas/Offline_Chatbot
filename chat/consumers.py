# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
from .ollama_client import AsyncOllamaClient
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            query = text_data_json['query']
            
            ollama_client = AsyncOllamaClient()
            await ollama_client.ask_query(query, self)
            
        except Exception as e:
            await self.send(json.dumps({
                "type": "error",
                "content": str(e)
            }))