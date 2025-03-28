# ollama_client.py
import aiohttp
import json

class AsyncOllamaClient:
    async def ask_query(self, prompt, websocket):
        url = "http://localhost:11434/api/generate"
        data = {
            "model": "llama3.2",
            "prompt": prompt,
            "stream": True
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data) as response:
                if response.status == 200:
                    async for line in response.content:
                        if line:
                            try:
                                json_data = json.loads(line)
                                text = json_data.get("response", "")
                                # Send each chunk immediately via WebSocket
                                await websocket.send(json.dumps({
                                    "type": "stream_chunk",
                                    "content": text,
                                    "done": json_data.get("done", False)
                                }))
                            except json.JSONDecodeError:
                                continue