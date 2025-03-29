"# Offline_Chatbot" 
# AI Chat Assistant with Ollama and Django

A real-time chat application powered by Ollama's Llama3 model, featuring WebSocket-based communication and markdown support.
See how working : https://drive.google.com/file/d/1jv7y5_voo3W93akte7JXrAtrqt2YMq8t/view?usp=sharing

## Features

- **Real-time Streaming**: Instant responses with token-by-token streaming
- **WebSocket Integration**: Efficient bidirectional communication
- **Markdown Support**: Code blocks, formatting, and rich text rendering
- **Typing Indicators**: Visual feedback during response generation
- **Responsive Design**: Works across desktop and mobile devices

## Prerequisites

- Python 3.9+
- Django 4.2+
- [Ollama](https://ollama.ai/) installed and running
- Node.js (for static file processing)
- aiohttp, channels, daphne, and other dependencies

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ollama-chat.git
   cd ollama-chat
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install django channels daphne aiohttp
   ```

4. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

6. **Ensure Ollama is running**
   ```bash
   ollama serve
   ```

7. **Pull the Llama3 model**
   ```bash
   ollama pull llama3
   ```

## Configuration

Update `settings.py` with your preferences:
```python
# chat/settings.py
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
SECRET_KEY = 'your-secret-key-here'
STATIC_URL = '/static/'
```

## Usage

1. Access the chat interface at `http://localhost:8000/chat/`
2. Type your message and press Enter
3. Receive real-time streaming responses
4. Use Shift+Enter for new lines

## Project Structure

```
.
├── chat/                  # Django app
│   ├── static/            # CSS, JS, images
│   ├── templates/         # HTML templates
│   ├── routing.py         # WebSocket routes
│   └── ollama_client.py   # AI integration
├── chatbot/               # Project config
│   ├── settings.py        # Django settings
│   └── asgi.py           # ASGI configuration
└── manage.py              # Django CLI
```

## Troubleshooting

**Ollama Connection Issues**
- Ensure Ollama is running: `ollama serve`
- Verify model availability: `ollama list`
- Check API endpoint: `http://localhost:11434/api/generate`

**WebSocket Errors**
- Confirm Daphne is installed
- Check ASGI configuration in `asgi.py`
- Verify WebSocket URL in chat.js

**Dependencies**
```bash
# If facing missing packages
pip install channels daphne aiohttp
```


