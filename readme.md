# Django Channels Chat Application

A real-time chat application built with Django, Channels, and WebSockets. Users can join chat rooms, pick a username, and send messages that are instantly broadcast to all participants in the room.

---

## Features

- Real-time messaging using WebSockets
- Join any chat room by name
- Prompt for username on room entry
- See notifications when users join a room
- Messages display sender's username

---

## Requirements

- Python 3.8+
- Django 4.x or 5.x
- channels
- uvicorn

---

## Setup Instructions

1. **Clone the repository or copy the project files to your machine.**

2. **Install dependencies:**

   ```bash
   pip install django channels "uvicorn[standard]"
   ```

3. **Apply migrations:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the development server (for HTTP):**

   ```bash
   python manage.py runserver
   ```

   > For WebSocket support, always use Uvicorn:

   ```bash
   uvicorn chatproject.asgi:application --reload --log-level debug --workers 1
   ```

5. **Open your browser and join a chat room:**
   ```
   http://127.0.0.1:8000/chat/lobby/
   ```
   Replace `lobby` with any room name you want.

---

## Project Structure

```
task3/
├── chatproject/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── chatapp/
│   ├── consumers.py
│   ├── models.py
│   ├── routing.py
│   ├── views.py
│   └── templates/
│       └── chatapp/
│           ├── room.html
│           └── home.html
├── db.sqlite3
└── manage.py
```

---

## How It Works

- When a user visits a chat room, they are prompted for a username.
- A "user joined" notification is broadcast to all users in the room.
- All messages are sent and received in real-time, with the sender's username displayed.

---

## Customization

- To add authentication, integrate Django's user system and use `self.scope["user"]` in the consumer.
- For production, use Redis as the channel layer backend.

---

## License

This project is for educational purposes.

---

## Credits

Built with [Django](https://www.djangoproject.com/) and [Channels](https://channels.readthedocs.io/).
