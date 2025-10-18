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

### Example Relationship Design

```json
// tasks
{
  "_id": "t123",
  "title": "Prepare report",
  "description": "Monthly financial report",
  "due_date": "2025-10-20",
  "status": "pending",
  "deleted": false
}

// categories
{
  "_id": "c101",
  "name": "Work",
  "description": "Office tasks"
}

// tags
{
  "_id": "tg501",
  "name": "urgent"
}

// tasks_categories
{
  "task_id": "t123",
  "category_id": "c101"
}

// tasks_tags
{
  "task_id": "t123",
  "tag_id": "tg501"
}


⚡ Installation
1. Clone the repository
git clone <repo_url>
cd task_board

2. Create a virtual environment and activate it
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Set environment variables
cp .env.example .env
# Update MongoDB URI and other settings in .env

5. Run the application
uvicorn app.main:app --reload


The API will be available at http://127.0.0.1:8000.