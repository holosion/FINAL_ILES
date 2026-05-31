# ILES Demo Credentials

Use these accounts for examiner testing. Create them with:

```powershell
cd backend
python manage.py migrate
python manage.py seed_demo
```

## Live system

| Service | URL |
|---|---|
| Frontend | https://final-iles.vercel.app |
| API root | https://iles-backend-magf.onrender.com/api/ |
| Dashboard API | https://iles-backend-magf.onrender.com/api/dashboard/ |

## Company (Workplace Supervisor)

| Field | Value |
|---|---|
| Email | demo.company@iles.test |
| Password | Company@2026 |
| Role | company |

After login: add student interns, create weekly reports, add supervisor comments.

## Lecturer (Academic Supervisor / Admin views)

| Field | Value |
|---|---|
| Email | demo.lecturer@iles.test |
| Password | Lecturer@2026 |
| Role | lecturer |

After login: open **Reports** to grade weekly reports (Makerere scale), open **Evaluations** for academic scores.

## Pre-seeded demo student

When `seed_demo` has been run:

| Field | Value |
|---|---|
| Name | Akena Jonathan |
| Registration | S21B13/001 |
| University | Makerere University |
| Company | Demo Tech Solutions |

The lecturer account can select this student under **Reports** and enter marks from 1–100.

## Verification note

Registration shows a demo verification code in the UI (email is not sent in this prototype). For seeded accounts, `is_verified=True` so login works immediately.
