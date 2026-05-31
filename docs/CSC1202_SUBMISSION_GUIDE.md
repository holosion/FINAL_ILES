# CSC 1202 Final Submission Guide — ILES

Use this checklist when preparing your PDF for MUELE. Keep explanations brief and attach screenshots for every item.

## Repository and deployment

| Item | Value |
|---|---|
| GitHub repository | https://github.com/holosion/FINAL_ILES.git |
| Live frontend | https://final-iles.vercel.app |
| Live API | https://iles-backend-magf.onrender.com/api |
| Submission deadline | 15 June 2026 |
| Keep live system active until | 31 August 2026 |

Demo login details: see [DEMO_CREDENTIALS.md](./DEMO_CREDENTIALS.md).

Seed demo data on Render (Shell or one-off job):

```bash
python manage.py seed_demo
```

## Module evidence map (35 marks)

| Module | Where it is implemented | Screenshot / API evidence |
|---|---|---|
| User & Role Management | `Login.jsx`, `Account` model, `/api/auth/*` | Login page, company vs lecturer dashboards, Postman register/verify/login |
| Internship Placement | `WeeklyLogs.jsx` student profile form, `StudentProfile` model | Add-intern form, `/api/students/` |
| Weekly Logbook | `WeeklyLogs.jsx` weekly report form, `WeeklyReport` model | Create report, attendance + activities fields |
| Supervisor Review Workflow | Company comments on reports, `WeeklyLog` status API (`/api/logs/`) | Company comment field, log status Draft→Approved in API |
| Academic Evaluation | `Evaluations.jsx`, `Evaluation` model | Three-score form, `/api/evaluations/` |
| Weighted Score Computation | `Reports.jsx`, `makerere_grade()` in `models.py` | Lecturer mark → grade, student `final_mark` average |
| Dashboards & Reporting | `Home.jsx`, `Reports.jsx`, `/api/dashboard/` | Dashboard cards, lecturer report summary |

## Role mapping for marking

| Guideline role | ILES account | Test flow |
|---|---|---|
| Student Intern | Managed via company account (`StudentProfile`) | Company adds intern, creates weekly reports |
| Workplace Supervisor | Company account (`role=company`) | Adds comments on weekly reports |
| Academic Supervisor | Lecturer account (`role=lecturer`) | Grades reports, opens Evaluations |
| Internship Administrator | Lecturer dashboard + Settings page | View stats, role overview, system settings |

## Testing evidence (10 marks)

Backend (pytest / Django test runner):

```powershell
cd backend
python manage.py test internship.tests
```

Frontend (Vitest + React Testing Library):

```powershell
cd frontend
npm test
```

Also capture:

- Postman or DRF browsable API: `https://iles-backend-magf.onrender.com/api/`
- Validation error responses (bad mark, bad attendance)
- Before/after screenshots for any bug fixes

## Git contribution evidence (20 marks)

Include in your PDF:

- Repository URL and contributor name: **holosion**
- Commit history screenshots (GitHub → Insights → Contributors, or Commits tab)
- Branch list and any pull requests
- Individual reflection (5 marks) — write this yourself

## Deployment evidence (5 marks)

- Render service dashboard screenshot
- Vercel project screenshot
- Environment variables (`VITE_API_BASE_URL`, `DATABASE_URL`, `SECRET_KEY`)
- Simple architecture:

```text
Browser → Vercel (React) → Render (Django API) → PostgreSQL
```

## Technical design evidence (5 marks)

Include short diagrams only:

- ERD: Account, StudentProfile, WeeklyReport, WeeklyLog, Evaluation
- Workflow: weekly report creation → company review → lecturer grading → final mark
- Architecture diagram (see above)

## PDF structure (recommended)

1. Cover page (names, registration numbers, repo URL, live URL)
2. Deployed system screenshots (login, dashboards, forms, reports)
3. Module evidence (one subsection per module, 1–2 screenshots each)
4. API evidence (Postman or Swagger/DRF)
5. Database evidence (Django admin or pgAdmin table view)
6. Git contribution screenshots
7. Test execution screenshots
8. Deployment screenshots + architecture diagram
9. Individual reflections

Avoid long theory sections. Marks come from working code, screenshots, and Git evidence.
