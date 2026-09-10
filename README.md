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

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Bhola-11/AI-Powered-Legal.git
   cd AI-Powered-Legal
   ```

2. **Set Up Python Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
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
