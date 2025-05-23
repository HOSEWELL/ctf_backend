# 🏆 CTF Judge Scoring System - Backend (Django)

This is the backend of a scoring system built using Django REST Framework for a technical screening challenge by CTFRoom. It manages judges, participants, and their scores, with APIs to support a frontend client (Next.js).

## ⚙️ Stack

- **Language**: Python 3.x  
- **Framework**: Django 4+  
- **REST API**: Django REST Framework  
- **Database**: SQLite (for development, switchable to MySQL/PostgreSQL)  
- **CORS**: django-cors-headers

---

## 📁 Project Structure
ctf/
├── api/ Main API app (Judges, Users, Scores)
├── ctf/ Django project settings
├── db.sqlite3 
├── manage.py
└── requirements.txt


## 🔧 Setup Instructions

### 1. Clone the Repo

git clone https://github.com/HOSEWELL/ctf-backend.git
cd ctf-backend
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver '''

Admin APIs-----

| Method | Endpoint       | Description     |
| ------ | -------------- | --------------- |
| POST   | `/api/judges/` | Add a new judge |
| GET    | `/api/judges/` | List all judges |

Judge APIs------------

| Method | Endpoint       | Description            |
| ------ | -------------- | ---------------------- |
| GET    | `/api/users/`  | List all participants  |
| POST   | `/api/scores/` | Assign score to a user |


Public APIs--------

| Method | Endpoint           | Description            |
| ------ | ------------------ | ---------------------- |
| GET    | `/api/scoreboard/` | View public scoreboard |
