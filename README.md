# 🧾 Employee Management System (Django REST Framework)

A simple and clean **Employee Management REST API** built using **Django REST Framework (DRF)**.  
It allows users to **Create**, **Read**, **Update**, **Delete**, **Search**, and **Export** employee data efficiently.  

---

## Features

- CRUD APIs for Employee management  
- Filter employees by department (`?department=IT`)  
- Search employees by name (`?search=John`)  
- Export employees as **CSV** or **JSON**  
- Swagger & Redoc API Documentation  
- SQLite database (inbuilt, no setup required)  
- Optional Docker support for containerization  

---

##  Tech Stack

- **Python 3.10+**  
- **Django 5.x**  
- **Django REST Framework (DRF)**  
- **drf-yasg** – Swagger documentation  
- **SQLite** (default database)  
- **Docker** (optional)

---

##  Project Structure
```bash
employee_management/
├── employee/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── employee_management/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Dockerfile
├── docker-compose.yml
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```
---

## Setup Instructions (using virtual enviroment)

### Clone the Repository

```bash
git clone https://github.com/hafismuhammed/employee_management.git
cd employee_management
```

### Create a Virtual Environment

```bash
python -m venv env
source env/bin/activate   # macOS/Linux
env\Scripts\activate      # Windows
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Run the Development server

```bash
python manage.py runserver
```

## 🐳 Docker Setup 
## Setup Instructions 

### Clone the Repository

```bash
git clone https://github.com/hafismuhammed/employee_management.git
cd employee_management
```

### Build and Run the Container

```bash
docker-compose up --build
```

## API documentation

 visit http://127.0.0.1:8000/swagger/




