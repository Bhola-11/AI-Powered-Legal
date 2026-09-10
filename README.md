# CivicLaw Enterprise: AI-Powered Legal Case Management & Court Workflow Platform

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

### Prerequisites
- Python 3.11+
- pip / poetry / pipenv

### Install Dependencies
```bash
pip install -r requirements.txt
# Or using make:
make install
```

### Build & Static Assets
```bash
python manage.py collectstatic --noinput
# Or using npm:
npm run build
# Or using make:
make build
```

### Database Migrations & Seeding
```bash
python manage.py migrate
python manage.py seed_civiclaw_data
```

### Run the Application

You can launch the platform using any of the following methods:

**Method 1: Direct Entry Point**
```bash
python main.py runserver 0.0.0.0:8000
```

**Method 2: WSGI App Runner**
```bash
python app.py
```

**Method 3: Manage Command**
```bash
python manage.py runserver 0.0.0.0:8000
```

**Method 4: Using Makefile / NPM**
```bash
make run
# or
npm start
```

**Method 5: Docker Container**
```bash
docker build -t civiclaw:latest .
docker run -p 8000:8000 civiclaw:latest
# or with docker-compose:
docker-compose up --build
```

Access the application in your browser at `http://127.0.0.1:8000/`.

---

## Running Automated Tests

```bash
python manage.py test tests
# Or using npm / make:
npm test
make test
```

---

## Build System & Entrypoints
- `main.py`: Primary application entrypoint
- `app.py`: Web service / WSGI runner entrypoint
- `Dockerfile`: Multi-stage container build definition
- `docker-compose.yml`: Local containerized deployment orchestrator
- `Makefile`: Build and automation tasks
- `package.json`: NPM build and start scripts
