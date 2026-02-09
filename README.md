# SQLAlchemy User Management Project

A beginner-friendly project to learn **SQLAlchemy ORM (2.0 style)** by building a simple **User Management System**.

---

## 📁 Project Structure

```sqlalchemy-user-management/
├── app/
│ ├── database.py # engine & session
│ ├── models.py # ORM models
│ ├── crud.py # CRUD operations
│ └── main.py # run & test
├── venv/
├── requirements.txt
└── users.db
```

---

## ⚙️ Setup

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
▶️ Run Project
python -m app.main
```

## 🧠 Concepts Practiced

SQLAlchemy Engine & Session\
Declarative ORM models\
CRUD operations\
Constraints (primary key, unique, not null)\
Defaults & timestamps\

## 🛠 Tech Stack

Python\
SQLAlchemy (ORM)\
SQLite\
