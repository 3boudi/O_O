# FastAPI Training Project

![Project Architecture](proto_work.png)

A simple training project built with **FastAPI** where you implemented CRUD operations, tested APIs, created models.

---

## 🚀 Overview
This project is a clean and minimal FastAPI setup designed to help you practice the fundamentals:

- Building REST APIs
- Connecting models with a database
- Creating CRUD operations
- Testing endpoints
- Organizing project structure

---

## 📂 Project Structure
```
project/

```

---

## ⚙️ Installation
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate   # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the server:
```bash
uvicorn main:app --reload
```

Server runs on:
```
http://127.0.0.1:8000
```

---

## 🗄️ Database Setup
The project uses **SQLModel** or **SQLAlchemy** (depends on your choice). Example database connection:
```python
engine = create_engine("sqlite:///database.db", echo=True)
```

---

## 🧪 Testing API
You tested the API using **FastAPI Docs** or **Postman**.

Interactive docs:
```
http://127.0.0.1:8000/docs
```

Alternative (ReDoc):
```
http://127.0.0.1:8000/redoc
```

---

## 🛠️ Technologies Used
- FastAPI
- Pydantic / SQLModel
- Uvicorn
- SQLite (or your chosen DB)
- Python 3.10+

---


