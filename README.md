# FinTrack Pro Backend

Backend service for **FinTrack Pro**, a full-stack personal finance management application.

Built using **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **JWT Authentication**, the API provides secure endpoints for authentication, transaction management, budgeting, financial goals, and analytics.

---

## Live API

**Base URL**

https://fintrack-pro-backend-met1.onrender.com

**API Documentation**

https://fintrack-pro-backend-met1.onrender.com/docs

---

## Features

* JWT-based authentication
* User registration and login
* Transaction management (CRUD)
* Budget management
* Financial goal tracking
* Analytics and spending insights
* PostgreSQL database integration
* Alembic database migrations
* RESTful API architecture
* Cloud deployment on Render

---

## Technology Stack

| Category         | Technology        |
| ---------------- | ----------------- |
| Language         | Python            |
| Framework        | FastAPI           |
| Database         | PostgreSQL (Neon) |
| ORM              | SQLAlchemy        |
| Migrations       | Alembic           |
| Authentication   | JWT (OAuth2)      |
| Validation       | Pydantic          |
| Password Hashing | Passlib (bcrypt)  |
| ASGI Server      | Uvicorn           |
| Deployment       | Render            |

---

## Architecture

```text
React + TypeScript Frontend
            │
            ▼
       FastAPI Backend
            │
            ▼
   PostgreSQL Database (Neon)
```

---

## Project Structure

```text
app/
├── api/
│   ├── auth.py
│   ├── transactions.py
│   ├── budgets.py
│   ├── goals.py
│   └── analytics.py
├── core/
│   ├── config.py
│   ├── dependencies.py
│   ├── jwt.py
│   └── security.py
├── db/
│   └── database.py
├── models/
│   ├── user.py
│   ├── transaction.py
│   ├── budget.py
│   └── goal.py
├── schemas/
└── main.py
```

---

## API Endpoints

### Authentication

| Method | Endpoint         |
| ------ | ---------------- |
| POST   | `/auth/register` |
| POST   | `/auth/login`    |

### Transactions

| Method | Endpoint             |
| ------ | -------------------- |
| GET    | `/transactions`      |
| POST   | `/transactions`      |
| PUT    | `/transactions/{id}` |
| DELETE | `/transactions/{id}` |

### Budgets

| Method | Endpoint   |
| ------ | ---------- |
| GET    | `/budgets` |
| POST   | `/budgets` |

### Goals

| Method | Endpoint      |
| ------ | ------------- |
| GET    | `/goals`      |
| POST   | `/goals`      |
| PUT    | `/goals/{id}` |
| DELETE | `/goals/{id}` |

### Analytics

| Method | Endpoint     |
| ------ | ------------ |
| GET    | `/analytics` |

---

## Deployment

| Component | Platform        |
| --------- | --------------- |
| Backend   | Render          |
| Database  | Neon PostgreSQL |

---

## Future Improvements

* Refresh token authentication
* Email verification
* Password reset
* Docker support
* Automated testing
* CI/CD pipeline
* Redis caching

---

## Author

**Aman Kanchan**

Developed as a portfolio project demonstrating backend development with FastAPI, REST API design, authentication, PostgreSQL, and cloud deployment.
