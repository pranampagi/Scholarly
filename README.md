# Scholarly: Research & Study Tracker

Scholarly is a lightweight, full-stack application designed to help researchers and students organize their academic resources.

## Features
- Track research papers
- Categorize by domain
- Manage study notes
- Status tracking (Pending, In Progress, Completed)

## Tech Stack
- **Backend:** FastAPI (Python)
- **Frontend:** Vue.js 3
- **Styling:** Bootstrap 5
- **Database:** SQLite (Development) / PostgreSQL (Production)
- **CI/CD:** GitHub Actions
- **Hosting:** Vercel

## Project Structure
```
.
├── backend/            # FastAPI application
├── frontend/           # Vue.js 3 application
├── README.md           # Project overview
```

## Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the development server:**
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.
   Explore the interactive documentation at `http://127.0.0.1:8000/docs`.

5. **Run tests:**
   ```bash
   python3 -m pytest tests/test_main.py
   ```

## API Endpoints

The API is fully documented using Swagger UI. Once the server is running, visit `http://127.0.0.1:8000/docs`.

### Resources
| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/resources/` | List all research resources (paginated). |
| `POST` | `/resources/` | Create a new research resource. |
| `PUT` | `/resources/{id}` | Update an existing resource. |
| `DELETE` | `/resources/{id}` | Delete a resource. |

## Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the development server:**
   ```bash
   npm run dev
   ```
   The application will be available at `http://localhost:5173`.

## Environment Variables
The frontend expects the backend to be running at `http://127.0.0.1:8000`. You can configure this in `frontend/src/services/api.js`.
