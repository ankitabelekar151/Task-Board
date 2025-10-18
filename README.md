# FastAPI TaskBoard Project

A **TaskBoard REST API** built using **FastAPI**, **Punq**, and **MongoDB** to manage tasks, categories, and tags. Each task can belong to multiple categories and tags. Relationships are managed via separate collections rather than embedding arrays. The project follows **clean architecture** principles and uses **Pydantic v2** for validation and responses.

---

## 🛠 Tech Stack

- **FastAPI** - Web framework  
- **Punq** - Dependency Injection  
- **Motor** - Async MongoDB driver  
- **Pydantic v2** - Data validation  
- **MongoDB** - NoSQL database  
- **Python 3.10+** - Async/await supported  

---

## 📦 Core Features

- **Create Category** - `POST /categories`  
- **Create Tag** - `POST /tags`  
- **Create Task** - `POST /tasks` (Relationships managed via separate collections)  
- **List Tasks** - `GET /tasks` (Filter by category or tag using cursor-based pagination)  
- **Update Task Status** - `PATCH /tasks/{task_id}/status`  
- **Delete Task** - Soft delete  

---

## 📂 Data Model (Conceptual)

### Collections

- `tasks`
- `categories`
- `tags`
- `tasks_categories` — `{ task_id, category_id }`
- `tasks_tags` — `{ task_id, tag_id }`

