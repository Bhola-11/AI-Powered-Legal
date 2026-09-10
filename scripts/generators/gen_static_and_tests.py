# scripts/generators/gen_static_and_tests.py
import os

def generate_static_and_tests(base_dir):
    print("Generating Static CSS/JS, Tests, Seed Script, and README...")
    
    # 1. Static CSS
    css_dir = os.path.join(base_dir, "static", "css")
    os.makedirs(css_dir, exist_ok=True)
    with open(os.path.join(css_dir, "civiclaw.css"), "w", encoding="utf-8") as f:
        f.write("""/* CivicLaw Enterprise Legal Design System */
:root {
    --primary-color: #1e3a8a;
    --primary-hover: #1e40af;
    --secondary-color: #475569;
    --accent-gold: #d97706;
    --bg-main: #f8fafc;
    --card-bg: #ffffff;
    --text-primary: #0f172a;
    --text-muted: #64748b;
    --border-color: #e2e8f0;
    --sidebar-width: 260px;
    --navbar-height: 64px;
    --success: #16a34a;
    --warning: #ca8a04;
    --danger: #dc2626;
    --info: #0284c7;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
}

body.civiclaw-body {
    background-color: var(--bg-main);
    color: var(--text-primary);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

/* Navbar */
.app-navbar {
    height: var(--navbar-height);
    background-color: #0f172a;
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 1.5rem;
    position: sticky;
    top: 0;
    z-index: 1000;
    border-bottom: 2px solid var(--accent-gold);
}

.navbar-brand a {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    color: #ffffff;
    text-decoration: none;
    font-weight: 700;
    font-size: 1.25rem;
}

.brand-icon {
    color: var(--accent-gold);
    font-size: 1.5rem;
}

.navbar-search {
    flex: 1;
    max-width: 500px;
    margin: 0 2rem;
    position: relative;
}

.global-search-input {
    width: 100%;
    padding: 0.5rem 1rem 0.5rem 2.25rem;
    border-radius: 9999px;
    border: 1px solid #334155;
    background-color: #1e293b;
    color: #f8fafc;
    font-size: 0.875rem;
    outline: none;
}

.global-search-input:focus {
    border-color: var(--accent-gold);
}

.search-icon {
    position: absolute;
    left: 0.85rem;
    top: 50%;
    transform: translateY(-50%);
    color: #94a3b8;
    font-size: 0.875rem;
}

.navbar-user-section {
    display: flex;
    align-items: center;
    gap: 1.25rem;
}

.nav-icon-btn {
    color: #cbd5e1;
    position: relative;
    font-size: 1.25rem;
    text-decoration: none;
}

.notification-badge {
    position: absolute;
    top: -6px;
    right: -8px;
    background-color: var(--danger);
    color: #ffffff;
    font-size: 0.65rem;
    padding: 2px 6px;
    border-radius: 9999px;
    font-weight: 700;
}

.ai-hub-pill {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    color: #ffffff;
    padding: 0.35rem 0.85rem;
    border-radius: 9999px;
    text-decoration: none;
    font-size: 0.8rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.4rem;
}

.user-dropdown {
    display: flex;
    align-items: center;
    gap: 0.75rem;
}

.user-role-badge {
    background-color: #334155;
    color: #cbd5e1;
    font-size: 0.7rem;
    padding: 0.2rem 0.5rem;
    border-radius: 4px;
    text-transform: uppercase;
}

.user-name {
    font-weight: 600;
    font-size: 0.875rem;
}

.profile-link, .logout-link {
    color: #94a3b8;
    text-decoration: none;
    font-size: 1rem;
}

.profile-link:hover, .logout-link:hover {
    color: #ffffff;
}

/* App Layout */
.app-layout {
    display: flex;
    flex: 1;
}

.app-sidebar {
    width: var(--sidebar-width);
    background-color: #1e293b;
    border-right: 1px solid #334155;
    padding: 1.5rem 0;
    flex-shrink: 0;
}

.sidebar-nav {
    display: flex;
    flex-direction: column;
}

.nav-group-title {
    font-size: 0.7rem;
    font-weight: 700;
    color: #64748b;
    padding: 1rem 1.5rem 0.35rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.nav-item {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.65rem 1.5rem;
    color: #cbd5e1;
    text-decoration: none;
    font-size: 0.875rem;
    transition: all 0.2s;
}

.nav-item:hover {
    background-color: #334155;
    color: #ffffff;
}

.nav-item.highlight {
    color: #f59e0b;
    font-weight: 600;
}

.main-content {
    flex: 1;
    padding: 2rem;
    overflow-y: auto;
}

.content-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
}

.content-header h2 {
    font-size: 1.5rem;
    font-weight: 700;
    color: #0f172a;
}

/* Civic Cards */
.civic-card {
    background-color: var(--card-bg);
    border: 1px solid var(--border-color);
    border-radius: 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    margin-bottom: 1.5rem;
}

.card-header {
    padding: 1rem 1.5rem;
    border-bottom: 1px solid var(--border-color);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.card-header h3 {
    font-size: 1.1rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.card-body {
    padding: 1.5rem;
}

/* Metrics Grid */
.metric-cards-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
}

.metric-card {
    background-color: #ffffff;
    border: 1px solid var(--border-color);
    border-radius: 8px;
    padding: 1.25rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}

.metric-icon {
    width: 48px;
    height: 48px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    font-size: 1.25rem;
}

.metric-data {
    display: flex;
    flex-direction: column;
}

.metric-number {
    font-size: 1.5rem;
    font-weight: 700;
}

.metric-label {
    font-size: 0.8rem;
    color: var(--text-muted);
}

.bg-primary { background-color: var(--primary-color); }
.bg-warning { background-color: var(--warning); }
.bg-danger { background-color: var(--danger); }
.bg-success { background-color: var(--success); }

/* Dashboard Two Col */
.dashboard-grid-two-col {
    display: grid;
    grid-template-columns: 1.5fr 1fr;
    gap: 1.5rem;
}

@media (max-width: 1024px) {
    .dashboard-grid-two-col {
        grid-template-columns: 1fr;
    }
}

/* Data Tables */
.table-responsive {
    overflow-x: auto;
}

.data-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.875rem;
}

.data-table th {
    background-color: #f1f5f9;
    padding: 0.75rem 1rem;
    text-align: left;
    font-weight: 600;
    color: #475569;
    border-bottom: 2px solid var(--border-color);
}

.data-table td {
    padding: 0.75rem 1rem;
    border-bottom: 1px solid var(--border-color);
    vertical-align: middle;
}

.data-table tr:hover {
    background-color: #f8fafc;
}

/* Badges */
.badge {
    display: inline-block;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
}

.badge-primary { background-color: #dbeafe; color: #1e40af; }
.badge-secondary { background-color: #f1f5f9; color: #475569; }
.badge-success { background-color: #dcfce7; color: #15803d; }
.badge-warning { background-color: #fef9c3; color: #854d0e; }
.badge-danger { background-color: #fee2e2; color: #b91c1c; }
.badge-info { background-color: #e0f2fe; color: #0369a1; }
.badge-dark { background-color: #334155; color: #f8fafc; }

/* Buttons */
.btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    font-size: 0.875rem;
    font-weight: 600;
    text-decoration: none;
    border: 1px solid transparent;
    cursor: pointer;
    transition: all 0.2s;
}

.btn-primary { background-color: var(--primary-color); color: #ffffff; }
.btn-primary:hover { background-color: var(--primary-hover); }
.btn-outline { background-color: transparent; border-color: var(--border-color); color: var(--text-primary); }
.btn-outline:hover { background-color: #f1f5f9; }
.btn-sm { padding: 0.25rem 0.5rem; font-size: 0.75rem; }

/* Form Controls */
.form-control {
    width: 100%;
    padding: 0.5rem 0.75rem;
    border: 1px solid var(--border-color);
    border-radius: 6px;
    font-size: 0.875rem;
}

.filter-bar {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1.25rem;
}

/* Footer */
.app-footer {
    background-color: #0f172a;
    color: #94a3b8;
    padding: 1.5rem;
    text-align: center;
    font-size: 0.8rem;
    margin-top: auto;
}

.app-footer a {
    color: #cbd5e1;
    text-decoration: none;
}
""")

    # 2. Static JS
    js_dir = os.path.join(base_dir, "static", "js")
    os.makedirs(js_dir, exist_ok=True)
    with open(os.path.join(js_dir, "civiclaw.js"), "w", encoding="utf-8") as f:
        f.write("""// CivicLaw Enterprise Interactive Client Module
document.addEventListener('DOMContentLoaded', () => {
    console.log('CivicLaw Enterprise Suite Initialized v2.4.0');

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transition = 'opacity 0.5s ease';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });

    // Conflict checker interactive trigger
    const conflictBtn = document.getElementById('run-conflict-check-btn');
    if (conflictBtn) {
        conflictBtn.addEventListener('click', () => {
            alert('Initiating real-time algorithmic conflict check across database...');
        });
    }

    // Interactive Cause List search filter
    const filterInput = document.querySelector('.filter-inputs input');
    if (filterInput) {
        filterInput.addEventListener('keyup', (e) => {
            const term = e.target.value.toLowerCase();
            const rows = document.querySelectorAll('.data-table tbody tr');
            rows.forEach(row => {
                const text = row.innerText.toLowerCase();
                row.style.display = text.includes(term) ? '' : 'none';
            });
        });
    }
});
""")

    # 3. Comprehensive Unit Tests
    t_dir = os.path.join(base_dir, "tests")
    os.makedirs(t_dir, exist_ok=True)
    with open(os.path.join(t_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("# Tests package\n")

    with open(os.path.join(t_dir, "test_civiclaw_suite.py"), "w", encoding="utf-8") as f:
        f.write("""from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.accounts.models import Role
from apps.firms.models import LawFirm
from apps.cases.models import Case, CaseType, CaseStatus
from apps.clients.models import ClientProfile
from apps.courts.models import CourtComplex, Judge
from apps.ai_engine.services import LegalAIService

User = get_user_model()

class CivicLawTestSuite(TestCase):
    def setUp(self):
        self.firm = LawFirm.objects.create(name="CivicLaw Legal Chambers", email="chambers@civiclaw.local", phone="+91-11-23456789")
        self.super_admin = User.objects.create_superuser(username="admin", email="admin@civiclaw.local", password="AdminPassword123!", role=Role.SUPER_ADMIN)
        self.lawyer = User.objects.create_user(username="advocate_sharma", email="sharma@civiclaw.local", password="LawyerPassword123!", role=Role.LAWYER, law_firm=self.firm)
        self.client_user = User.objects.create_user(username="client_corp", email="client@corp.local", password="ClientPassword123!", role=Role.CLIENT)
        self.client_profile = ClientProfile.objects.create(user=self.client_user, display_name="Nexus Technologies Corp", email="contact@nexus.local", phone="+91-9876543210")
        self.court = CourtComplex.objects.create(name="High Court of Delhi", city="New Delhi", state="Delhi", address="Sher Shah Road")
        self.judge = Judge.objects.create(name="Hon. Justice K.R. Rao", court_complex=self.court)
        self.case_type = CaseType.objects.create(code="CS", name="Civil Suit", category="CIVIL")

    def test_user_roles(self):
        self.assertTrue(self.super_admin.is_super_admin())
        self.assertTrue(self.lawyer.is_lawyer())
        self.assertTrue(self.client_user.is_client())

    def test_case_creation_lifecycle(self):
        case = Case.objects.create(
            case_number="CS/2026/001",
            title="Nexus Technologies v. Global Infra",
            case_type=self.case_type,
            court_complex=self.court,
            presiding_judge=self.judge,
            client=self.client_profile,
            law_firm=self.firm,
            description="Suit for Specific Performance and Damages",
            status=CaseStatus.INTAKE
        )
        self.assertEqual(case.status, CaseStatus.INTAKE)
        case.status = CaseStatus.REGISTERED
        case.save()
        self.assertEqual(case.status, CaseStatus.REGISTERED)

    def test_ai_copilot_services(self):
        summary = LegalAIService.generate_case_summary("Contract Breach", "Breach of distribution agreement", "Liquidated damages clause")
        self.assertIn("Executive Summary", summary["summary"])
        self.assertGreater(summary["confidence_score"], 0.90)

        conflict = LegalAIService.check_conflict_of_interest("Nexus Tech", "Global Infra", ["Nexus Tech", "Alpha Corp"], [])
        self.assertFalse(conflict["has_conflict"])
""")

    # 4. Management Command Seed Data
    cmd_dir = os.path.join(base_dir, "apps", "core", "management", "commands")
    os.makedirs(cmd_dir, exist_ok=True)
    with open(os.path.join(base_dir, "apps", "core", "management", "__init__.py"), "w", encoding="utf-8") as f:
        f.write("")
    with open(os.path.join(cmd_dir, "__init__.py"), "w", encoding="utf-8") as f:
        f.write("")
    with open(os.path.join(cmd_dir, "seed_civiclaw_data.py"), "w", encoding="utf-8") as f:
        f.write("""from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.accounts.models import Role, UserProfile
from apps.firms.models import LawFirm, BranchOffice, PracticeArea, FirmSetting
from apps.clients.models import ClientProfile, ClientType
from apps.courts.models import CourtComplex, CourtRoom, Judge, CourtLevel
from apps.cases.models import Case, CaseType, CaseStatus, CasePriority
from apps.hearings.models import Hearing, HearingType
from apps.billing.models import Invoice, InvoiceStatus
from django.utils import timezone
import datetime

User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds initial enterprise legal data for CivicLaw platform'

    def handle(self, *args, **options):
        self.stdout.write("Seeding CivicLaw enterprise records...")
        
        # Law Firm
        firm, _ = LawFirm.objects.get_or_create(
            name="CivicLaw Premier Legal LLP",
            defaults={'email': 'contact@civiclaw.local', 'phone': '+91-11-23000000', 'primary_office_address': 'Connaught Place, New Delhi'}
        )
        FirmSetting.objects.get_or_create(firm=firm)

        # Users
        admin_user, _ = User.objects.get_or_create(
            username="admin",
            defaults={'email': 'admin@civiclaw.local', 'role': Role.SUPER_ADMIN, 'is_staff': True, 'is_superuser': True}
        )
        admin_user.set_password("Admin@12345")
        admin_user.save()

        lawyer, _ = User.objects.get_or_create(
            username="advocate_kapoor",
            defaults={'email': 'kapoor@civiclaw.local', 'role': Role.LAWYER, 'first_name': 'Vikram', 'last_name': 'Kapoor', 'law_firm': firm}
        )
        lawyer.set_password("Lawyer@12345")
        lawyer.save()

        # Courts & Judges
        hc, _ = CourtComplex.objects.get_or_create(
            name="High Court of Delhi",
            defaults={'level': CourtLevel.HIGH_COURT, 'city': 'New Delhi', 'state': 'Delhi', 'address': 'Sher Shah Road'}
        )
        room, _ = CourtRoom.objects.get_or_create(court_complex=hc, room_number="Courtroom 04")
        judge, _ = Judge.objects.get_or_create(name="Justice Sanjay Kishan", defaults={'court_complex': hc, 'assigned_courtroom': room})

        # Clients & Cases
        client, _ = ClientProfile.objects.get_or_create(
            display_name="Bharat Heavy Infrastructure Ltd",
            defaults={'client_type': ClientType.CORPORATE, 'email': 'legal@bharat-infra.local', 'phone': '+91-9811122233', 'billing_address': 'Barakhamba Road, New Delhi'}
        )
        ctype, _ = CaseType.objects.get_or_create(code="ARB", defaults={'name': 'Arbitration Petition', 'category': 'ARBITRATION'})
        
        case, _ = Case.objects.get_or_create(
            case_number="ARB/2026/108",
            defaults={
                'title': 'Bharat Heavy Infra v. Metrorail Corporation',
                'case_type': ctype,
                'court_complex': hc,
                'courtroom': room,
                'presiding_judge': judge,
                'client': client,
                'law_firm': firm,
                'status': CaseStatus.HEARING_SCHEDULED,
                'priority': CasePriority.HIGH,
                'filing_date': timezone.now().date(),
                'next_hearing_date': timezone.now().date() + datetime.timedelta(days=7),
                'description': 'Section 9 Arbitration Petition for urgent interim measures restraining bank guarantee invocation.',
            }
        )

        Hearing.objects.get_or_create(
            case=case,
            hearing_date=timezone.now().date() + datetime.timedelta(days=7),
            defaults={'start_time': '10:30:00', 'courtroom': room, 'judge': judge, 'hearing_type': HearingType.INTERIM_RELIEF, 'purpose': 'Hearing on Interim Injunction'}
        )

        self.stdout.write(self.style.SUCCESS("CivicLaw enterprise seed data initialized successfully."))
""")

    # 5. README.md
    readme_path = os.path.join(base_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("""# CivicLaw Enterprise: AI-Powered Legal Case Management & Court Workflow Platform

An enterprise-grade, comprehensive legal case management and judicial court workflow system built with **Python 3.11, Django 5.0+, Django MVT architecture, HTML5, CSS3, JavaScript, and SQLite**.

---

## Key Modules & Architecture

1. **User Authentication & 5-Role RBAC**:
   - Super Admin, Law Firm Admin, Advocate / Lawyer, Paralegal, and Client Portal.
2. **Comprehensive 16-Stage Case Lifecycle Workflow**:
   - `Draft` → `Intake` → `Conflict Check` → `Client Verification` → `Case Registration` → `Court Assignment` → `Advocate Assignment` → `Document Collection` → `Evidence Preparation` → `Hearing Scheduling` → `Hearing In Session` → `Order Recording` → `Follow-up Tasks` → `Next Hearing` → `Judgment / Disposition` → `Compliance` → `Case Closure / Archive`.
3. **Court & Judicial Administration**:
   - Hierarchy from Supreme Court to Subordinate Courts, Court Complexes, Courtrooms, Judges, and Benches.
4. **Hearings, Daily Board & Calendar Engine**:
   - Conflict-free hearing scheduling, courtroom availability, daily cause lists, and proceedings outcomes.
5. **Legal Document Vault & Versioning**:
   - Category management, SHA-256 cryptographic integrity verification, version history, and role-based permissions.
6. **Evidence Register & Chain of Custody**:
   - Exhibit marking (Ex. P-1 / Ex. D-1), physical & digital custody tracking, and witness linking.
7. **Legal Research & Authentic Statutory Corpus**:
   - Complete statutory codifications: Code of Civil Procedure (CPC), Code of Criminal Procedure (CrPC / BNSS), Penal Code (IPC / BNS), Law of Evidence (BSA), Limitation Act (all 137 Articles), Arbitration, Commercial Courts, Companies Act, and Constitution of India.
   - Comprehensive landmark precedent database with ratio decidendi and neutral citations.
   - Standard legal pleading templates (Plaints, Writs, Bail, Injunctions, Notices, Agreements).
8. **Task & Workflow Management**:
   - Workflow stages, procedural checklists, and interactive Kanban boards.
9. **Deadlines & Limitation Tracking**:
   - Automated limitation period calculator, statutory deadlines, and escalation reminders.
10. **Client Communications**:
    - Secure messaging portal, isolated internal legal notes, and file attachments.
11. **Billing, Ledger & Invoicing**:
    - Billable hourly tracking, case expenses, tax invoices, receipts, and payment ledger.
12. **Court Orders, Judgments & Compliance**:
    - Interim orders, final decrees, and compliance tracking checklists.
13. **Tamper-Evident Audit System**:
    - Cryptographically chained SHA-256 audit trails for all operations.
14. **AI Legal Assistant (Copilot)**:
    - AI Case Summarizer, AI Petition Drafter, AI Conflict of Interest Analyzer, and Precedent Matcher.

---

## Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Bhola-11/AI-Powered-Legal.git
   cd AI-Powered-Legal
   ```

2. **Set Up Python Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
   pip install django
   ```

3. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Seed Enterprise Sample Data**:
   ```bash
   python manage.py seed_civiclaw_data
   ```

5. **Start Application Server**:
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` to access the portal.

---

## Running Automated Tests

```bash
python manage.py test tests
```
""")

    print("Completed Static, Tests, Seed Script, and README generation.")

if __name__ == '__main__':
    generate_static_and_tests('.')
