# 🎓 Scholarly: Research & Study Tracker

**Scholarly** is a professional, full-stack application designed to help researchers, students, and lifelong learners organize their academic resources. Effortlessly track research papers, categorize them by domain (e.g., Machine Learning, GATE CS), and manage your study progress with a modern, aesthetic dashboard.

---

## 🌟 Key Features

- **Resource Management:** Add, edit, and delete research papers or study links.
- **Dynamic Filtering:** Instantly filter your library by category (discovered dynamically from your data).
- **Real-time Search:** Find any resource by title with a lightning-fast search bar.
- **Status Tracking:** Visual badges for *Pending*, *In Progress*, and *Completed* items.
- **Responsive Design:** Premium UI built with Bootstrap 5, fully optimized for mobile and desktop.
- **Statistics API:** Built-in analytics endpoint to track your library growth.

---

## 🛠 Tech Stack

- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python 3.11)
- **Frontend:** [Vue.js 3](https://vuejs.org/) (Vite)
- **Styling:** [Bootstrap 5](https://getbootstrap.com/) + [Bootstrap Icons](https://icons.getbootstrap.com/)
- **Database:** SQLite (Local) / PostgreSQL (Production)
- **CI/CD:** [GitHub Actions](https://github.com/features/actions)
- **Deployment:** [Vercel](https://vercel.com/) (Optimized for Monorepos)

---

## 📂 Project Structure

```text
.
├── .github/workflows/  # CI/CD pipeline (Testing & Build)
├── backend/            # FastAPI source code & Unit tests
├── frontend/           # Vue.js 3 dashboard (Vite)
├── vercel.json         # Production deployment config
└── scholarly.db        # Local SQLite database
```

---

## 🚀 Quick Start

### Backend (API)
1. `cd backend`
2. `python -m venv .venv && source .venv/bin/activate`
3. `pip install -r requirements.txt`
4. `uvicorn main:app --reload`
   - *API Docs:* `http://127.0.0.1:8000/docs`

### Frontend (Dashboard)
1. `cd frontend`
2. `npm install`
3. `npm run dev`
   - *Dashboard:* `http://localhost:5173`

---

## 📡 API Documentation

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/resources/` | List all research resources (paginated). |
| `POST` | `/resources/` | Create a new research resource. |
| `PUT` | `/resources/{id}` | Update an existing resource details. |
| `DELETE` | `/resources/{id}` | Remove a resource from the library. |
| `GET` | `/stats/` | **[New]** Get library stats by category/status. |

---

## ⚙️ CI/CD & Deployment

### GitHub Actions
This project includes an automated pipeline that runs on every push:
- **Backend:** Validates all CRUD logic using `pytest`.
- **Frontend:** Ensures the production build compiles successfully.

### Vercel Deployment
The root `vercel.json` is pre-configured for a seamless monorepo deployment. When connected to Vercel:
- `/api/*` requests are handled by the FastAPI server.
- All other requests serve the static Vue.js frontend.

---

## 📄 License
MIT License. Feel free to use and adapt this for your own research tracking!
