# M.A.R.S — Management and Request System

A document request management system for **La Union Senior High School**. Students can submit and track document requests online; staff and administrators manage processing, pickup scheduling, and document digitization.

## Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | Vue 3 (Composition API), Vite, Vue Router 5, Pinia, Tailwind CSS v4, Chart.js, Axios |
| **Backend** | Django 5.2, Django REST Framework (DRF), SimpleJWT, Gunicorn |
| **Database** | PostgreSQL (Supabase) |
| **Deployment** | Frontend: Vercel — Backend: Render |

## System Roles

- **Student (Requestor)** — submits document requests, tracks status via passkey
- **Staff** — manages requests, uploads processed documents, manages pickup slots, views student directory
- **Admin/Superuser** — full CRUD on requests, students, staff, document types, strands, pickup slots, audit logs

## Features

- Public request submission with pickup scheduling
- Request tracking via unique passkey
- Two‑tier authentication (Staff JWT + Admin JWT)
- Dashboard analytics with charts (strand breakdown, document breakdown, monthly trends)
- Document management: student uploads, processed documents, master digitized records
- Pickup slot calendar (30‑day view with capacity management)
- Email notifications (Gmail SMTP) for submission confirmation and status updates
- Audit logging for all admin/staff actions
- Student master record management with document attachments
- Bulk request status updates
- Student record checking before submission
- Duplicate request prevention

## Project Structure

```
mars_request/       # Vue 3 frontend
mars_backend/       # Django REST backend
vercel.json         # Vercel deployment config
```

## Local Development

### Backend

```bash
cd mars_backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The API runs at `http://127.0.0.1:8000/api/`.

### Frontend

```bash
cd mars_request
npm install
npm run dev
```

The app runs at `http://localhost:5173/` and proxies API calls to `http://127.0.0.1:8000/api/`.

### Default Admin

On fresh deploy (Render), an admin user is auto‑created:

- **URL:** `https://mars-launion.onrender.com/admin/`
- **Username:** `admin`
- **Password:** `admin`

## Deployment

### Backend (Render)

| Setting | Value |
|---|---|
| **Root Directory** | `mars_backend` |
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn mars_backend.wsgi` |
| **Region** | Singapore |

**Environment Variables:**

| Name | Value |
|---|---|
| `RENDER` | `true` |
| `SECRET_KEY` | Generate a random key |
| `DATABASE_URL` | Supabase PostgreSQL connection string |

### Frontend (Vercel)

| Setting | Value |
|---|---|
| **Root Directory** | `mars_request` |
| **Framework Preset** | Vite |

**Environment Variable:**

| Name | Value |
|---|---|
| `VITE_API_URL` | `https://mars-launion.onrender.com/api/` |

### Database (Supabase)

- Region: Singapore
- Connection: Session pooler on port 6543
- SSL required in production

## API Endpoints

### Public
- `POST /api/requests/` — Submit a new request
- `GET /api/requests/lookup/<code>/` — Look up request by code
- `GET /api/public/document-types/` — Active document types
- `GET /api/public/strands/` — All strands
- `GET /api/public/slots/` — Available pickup slots
- `GET /api/public/my-request/?passkey=...` — Check request by passkey
- `GET /api/public/check-record/` — Check student record

### Auth
- `POST /api/register/` — Register staff
- `POST /api/login/` — Obtain JWT tokens
- `POST /api/token/refresh/` — Refresh JWT token

### Admin (authenticated)
- `GET/POST /api/admin/stats/` — Dashboard statistics
- `GET/POST /api/admin/requests/` — List/create requests
- `PATCH /api/admin/requests/<id>/` — Update request
- `POST /api/admin/requests/bulk/` — Bulk update statuses
- `CRUD /api/admin/document-types/` — Document type management
- `CRUD /api/admin/strands/` — Strand management
- `CRUD /api/admin/staff/` — Staff account management
- `CRUD /api/admin/slots/` — Pickup slot management
- `CRUD /api/admin/students/` — Student record management
- `GET /api/admin/audit-logs/` — System audit logs
- `POST /api/admin/requests/<id>/documents/` — Upload student document
- `POST /api/admin/requests/<id>/processed/` — Upload processed document
- `POST /api/admin/students/<id>/documents/` — Upload master document

## Keep‑Alive

Render free tier sleeps after 15 minutes of inactivity. Use [cron-job.org](https://cron-job.org) to ping `https://mars-launion.onrender.com/admin/login/` every 14 minutes to keep it awake.
