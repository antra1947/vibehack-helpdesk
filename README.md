 VibeHack Helpdesk
VibeHack Helpdesk is a Django-based ticket management web application designed to simplify issue tracking and user support during hackathons or collaborative projects.
It allows users to create, manage, and resolve tickets, while admins can monitor and prioritize issues efficiently.

🚀 Live Demo
🔗 https://vibehack-helpdesk.onrender.com

🛠️ Tech Stack
Backend: Python, Django

Frontend: HTML, CSS, JavaScript

Database: SQLite (or PostgreSQL if deployed)

Server: Gunicorn

Hosting: Render

💡 Features
✅ User signup and login (public access)
✅ Create, edit, and delete support tickets
✅ Prioritize issues as Low, Medium, or High
✅ Admin dashboard for managing all tickets
✅ Responsive, simple UI using Django templates
✅ Deployed and live using Render

⚙️ Installation (For Local Setup)
Clone the repository

git clone https://github.com/antra1947/vibehack-helpdesk.git
cd vibehack-helpdesk
Create virtual environment

python -m venv venv
source venv/bin/activate     # For macOS/Linux
venv\Scripts\activate        # For Windows
Install dependencies

pip install -r requirements.txt
Run migrations

python manage.py migrate
Run the server

python manage.py runserver
Open in browser

http://127.0.0.1:8000/
🌐 Deployment Details (Render)
Start Command:

gunicorn mysite.wsgi:application
Environment Variables:

SECRET_KEY = django-insecure-dev-secret-key
DEBUG = False
Hosted URL:
https://vibehack-helpdesk.onrender.com

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

📧 Contact
👩‍💻 Developed by: Antra Gupta
📬 Email: [antra1947@gmail.com]
🔗 GitHub: https://github.com/antra1947
