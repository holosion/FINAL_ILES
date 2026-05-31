"""Load demo accounts and sample internship data for CSC 1202 testing."""

from datetime import date, timedelta

from django.core.management.base import BaseCommand

from internship.models import Account, Evaluation, StudentProfile, WeeklyLog, WeeklyReport


class Command(BaseCommand):
    help = "Create verified demo company/lecturer accounts and sample internship records."

    def handle(self, *args, **options):
        company, created = self._get_or_create_account(
            role=Account.ROLE_COMPANY,
            email="demo.company@iles.test",
            password="Company@2026",
            name="Demo Tech Solutions",
            company_name="Demo Tech Solutions",
        )
        lecturer, lecturer_created = self._get_or_create_account(
            role=Account.ROLE_LECTURER,
            email="demo.lecturer@iles.test",
            password="Lecturer@2026",
            name="Dr. Demo Lecturer",
        )

        student, student_created = StudentProfile.objects.get_or_create(
            company=company,
            registration_number="S21B13/001",
            defaults={
                "name": "Akena Jonathan",
                "university": "Makerere University",
                "internship_months": 3,
            },
        )

        week_start = date.today() - timedelta(days=14)
        report, report_created = WeeklyReport.objects.get_or_create(
            student=student,
            week_number=1,
            defaults={
                "week_start": week_start,
                "week_end": week_start + timedelta(days=6),
                "attendance_days": 5,
                "activities": "Configured React pages, tested Django API endpoints, and prepared deployment docs.",
                "company_comments": "Good progress on the internship logbook module.",
                "lecturer_mark": 85,
                "lecturer_comments": "Solid weekly reflection.",
            },
        )

        log, log_created = WeeklyLog.objects.get_or_create(
            week=1,
            defaults={
                "activity": "Submitted internship logbook entry for supervisor review.",
                "status": WeeklyLog.STATUS_REVIEWED,
            },
        )

        evaluation, evaluation_created = Evaluation.objects.get_or_create(
            student="Akena Jonathan",
            defaults={
                "technical": 82,
                "communication": 78,
                "attendance": 90,
            },
        )

        self.stdout.write(self.style.SUCCESS("Demo data ready."))
        self.stdout.write(f"  Company: demo.company@iles.test / Company@2026 ({'new' if created else 'existing'})")
        self.stdout.write(f"  Lecturer: demo.lecturer@iles.test / Lecturer@2026 ({'new' if lecturer_created else 'existing'})")
        self.stdout.write(f"  Student: {student.name} ({'new' if student_created else 'existing'})")
        self.stdout.write(f"  Weekly report week 1 ({'new' if report_created else 'existing'})")
        self.stdout.write(f"  Weekly log ({'new' if log_created else 'existing'})")
        self.stdout.write(f"  Evaluation ({'new' if evaluation_created else 'existing'})")

    def _get_or_create_account(self, role, email, password, name, company_name=""):
        account, created = Account.objects.get_or_create(
            email=email,
            defaults={
                "role": role,
                "name": name,
                "company_name": company_name,
                "is_verified": True,
                "verification_code": "",
            },
        )
        if created or not account.is_verified:
            account.role = role
            account.name = name
            account.company_name = company_name
            account.is_verified = True
            account.set_password(password)
            account.save()
        return account, created
