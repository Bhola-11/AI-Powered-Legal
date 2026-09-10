# scripts/generators/gen_all_templates.py
import os

def generate_templates(base_dir):
    print("Generating Django MVT Templates...")
    tpl_dir = os.path.join(base_dir, "templates")
    os.makedirs(tpl_dir, exist_ok=True)

    # 1. Base layouts
    with open(os.path.join(tpl_dir, "base.html"), "w", encoding="utf-8") as f:
        f.write("""{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}CivicLaw Enterprise{% endblock %} - AI Legal Suite</title>
    <link rel="stylesheet" href="{% static 'css/civiclaw.css' %}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    {% block extra_css %}{% endblock %}
</head>
<body class="civiclaw-body">
    {% include 'navbar.html' %}
    <div class="app-layout">
        {% include 'sidebar.html' %}
        <main class="main-content">
            {% include 'messages.html' %}
            <div class="content-header">
                <h2>{% block page_title %}{% endblock %}</h2>
                <div class="header-actions">
                    {% block header_actions %}{% endblock %}
                </div>
            </div>
            <div class="content-body">
                {% block content %}{% endblock %}
            </div>
        </main>
    </div>
    {% include 'footer.html' %}
    <script src="{% static 'js/civiclaw.js' %}"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
""")

    with open(os.path.join(tpl_dir, "navbar.html"), "w", encoding="utf-8") as f:
        f.write("""<header class="app-navbar">
    <div class="navbar-brand">
        <a href="{% url 'accounts:dashboard_redirect' %}">
            <i class="fa-solid fa-scale-balanced brand-icon"></i>
            <span class="brand-title">{{ PLATFORM_NAME }}</span>
        </a>
    </div>
    <div class="navbar-search">
        <form action="{% url 'cases:case_list' %}" method="get">
            <i class="fa-solid fa-magnifying-glass search-icon"></i>
            <input type="text" name="q" placeholder="Global Search: Case number, Party, Court, Judge..." class="global-search-input">
        </form>
    </div>
    <div class="navbar-user-section">
        {% if user.is_authenticated %}
            <a href="{% url 'notifications:notification_list' %}" class="nav-icon-btn" title="Notifications">
                <i class="fa-solid fa-bell"></i>
                <span class="notification-badge">3</span>
            </a>
            <a href="{% url 'ai_engine:ai_hub' %}" class="ai-hub-pill">
                <i class="fa-solid fa-wand-magic-sparkles"></i> AI Copilot
            </a>
            <div class="user-dropdown">
                <span class="user-role-badge">{{ user.get_role_display }}</span>
                <span class="user-name">{{ user.get_full_name|default:user.username }}</span>
                <a href="{% url 'accounts:profile' %}" class="profile-link" title="Profile"><i class="fa-solid fa-user-gear"></i></a>
                <a href="{% url 'accounts:logout' %}" class="logout-link" title="Logout"><i class="fa-solid fa-arrow-right-from-bracket"></i></a>
            </div>
        {% else %}
            <a href="{% url 'accounts:login' %}" class="btn btn-primary">Login</a>
        {% endif %}
    </div>
</header>
""")

    with open(os.path.join(tpl_dir, "sidebar.html"), "w", encoding="utf-8") as f:
        f.write("""<aside class="app-sidebar">
    <nav class="sidebar-nav">
        <div class="nav-group-title">MAIN NAVIGATION</div>
        <a href="{% url 'accounts:dashboard_redirect' %}" class="nav-item">
            <i class="fa-solid fa-gauge-high"></i> Dashboard
        </a>
        <a href="{% url 'cases:case_list' %}" class="nav-item">
            <i class="fa-solid fa-briefcase"></i> Case Management
        </a>
        <a href="{% url 'cases:case_intake' %}" class="nav-item">
            <i class="fa-solid fa-file-circle-plus"></i> Case Intake Wizard
        </a>
        <a href="{% url 'hearings:hearing_list' %}" class="nav-item">
            <i class="fa-solid fa-gavel"></i> Hearings & Calendar
        </a>
        <a href="{% url 'hearings:daily_board' %}" class="nav-item">
            <i class="fa-solid fa-calendar-day"></i> Daily Board
        </a>

        <div class="nav-group-title">LEGAL OPERATIONS</div>
        <a href="{% url 'documents:vault' %}" class="nav-item">
            <i class="fa-solid fa-folder-open"></i> Document Vault
        </a>
        <a href="{% url 'evidence:register' %}" class="nav-item">
            <i class="fa-solid fa-fingerprint"></i> Evidence Register
        </a>
        <a href="{% url 'tasks:task_list' %}" class="nav-item">
            <i class="fa-solid fa-list-check"></i> Tasks & Workflows
        </a>
        <a href="{% url 'tasks:kanban' %}" class="nav-item">
            <i class="fa-solid fa-table-columns"></i> Task Kanban
        </a>
        <a href="{% url 'deadlines:deadline_list' %}" class="nav-item">
            <i class="fa-solid fa-clock"></i> Deadlines & Limitation
        </a>
        <a href="{% url 'orders_judgments:order_list' %}" class="nav-item">
            <i class="fa-solid fa-stamp"></i> Court Orders & Decrees
        </a>

        <div class="nav-group-title">RESEARCH & INTELLIGENCE</div>
        <a href="{% url 'ai_engine:ai_hub' %}" class="nav-item highlight">
            <i class="fa-solid fa-brain"></i> AI Legal Assistant
        </a>
        <a href="{% url 'legal_research:acts_list' %}" class="nav-item">
            <i class="fa-solid fa-book-bookmark"></i> Statutory Codes
        </a>
        <a href="{% url 'legal_research:precedent_list' %}" class="nav-item">
            <i class="fa-solid fa-landmark"></i> Precedents Library
        </a>
        <a href="{% url 'legal_research:notebook' %}" class="nav-item">
            <i class="fa-solid fa-pen-to-square"></i> Research Notebooks
        </a>

        <div class="nav-group-title">CLIENTS & BILLING</div>
        <a href="{% url 'clients:client_list' %}" class="nav-item">
            <i class="fa-solid fa-users"></i> Clients Registry
        </a>
        <a href="{% url 'clients:conflict_check' %}" class="nav-item">
            <i class="fa-solid fa-shield-halved"></i> Conflict Clearance
        </a>
        <a href="{% url 'communications:thread_list' %}" class="nav-item">
            <i class="fa-solid fa-comments"></i> Secure Messages
        </a>
        <a href="{% url 'billing:invoice_list' %}" class="nav-item">
            <i class="fa-solid fa-file-invoice-dollar"></i> Billing & Invoices
        </a>
        <a href="{% url 'billing:time_entries' %}" class="nav-item">
            <i class="fa-solid fa-stopwatch"></i> Billable Hours
        </a>

        <div class="nav-group-title">ADMINISTRATION</div>
        <a href="{% url 'courts:court_list' %}" class="nav-item">
            <i class="fa-solid fa-building-columns"></i> Courts & Judges
        </a>
        <a href="{% url 'analytics:reports_dashboard' %}" class="nav-item">
            <i class="fa-solid fa-chart-line"></i> Analytics & Reports
        </a>
        <a href="{% url 'audit:audit_log_view' %}" class="nav-item">
            <i class="fa-solid fa-shield-virus"></i> Tamper-Evident Audit
        </a>
    </nav>
</aside>
""")

    with open(os.path.join(tpl_dir, "footer.html"), "w", encoding="utf-8") as f:
        f.write("""<footer class="app-footer">
    <div class="footer-content">
        <p>&copy; 2026 {{ PLATFORM_NAME }} | {{ PLATFORM_TAGLINE }} | Version {{ PLATFORM_VERSION }}</p>
        <p class="footer-links">
            <a href="#">Compliance</a> &bull;
            <a href="#">Security & Encryption</a> &bull;
            <a href="#">National Judicial Data Grid Sync</a>
        </p>
    </div>
</footer>
""")

    with open(os.path.join(tpl_dir, "messages.html"), "w", encoding="utf-8") as f:
        f.write("""{% if messages %}
<div class="messages-container">
    {% for message in messages %}
    <div class="alert alert-{{ message.tags }}">
        <i class="fa-solid fa-circle-info"></i> {{ message }}
    </div>
    {% endfor %}
</div>
{% endif %}
""")

    # 2. Dashboards for 5 roles
    d_dir = os.path.join(tpl_dir, "dashboards")
    os.makedirs(d_dir, exist_ok=True)
    roles = [
        ("super_admin.html", "Super Admin Command Center", "System-wide operational oversight, multi-tenant law firm monitoring, judicial court complexes, and security audits."),
        ("firm_admin.html", "Law Firm Managing Partner Dashboard", "Practice area workloads, billable realization, case disposition rates, lawyer assignments, and client billing."),
        ("lawyer.html", "Advocate / Senior Counsel Workspace", "Assigned cases, today's cause lists, hearing outcomes, drafting deadlines, and evidence preparation."),
        ("paralegal.html", "Paralegal / Legal Assistant Workflow Hub", "Case file preparation, document filing, exhibit tagging, chain-of-custody logging, and calendar scheduling."),
        ("client.html", "Client Legal Portal", "Secure matter tracking, hearing schedules, approved filings, client-counsel communications, and invoices."),
    ]
    for fname, title, desc in roles:
        content = """{% extends 'base.html' %}
{% block title %}__TITLE__{% endblock %}
{% block page_title %}__TITLE__{% endblock %}

{% block content %}
<div class="dashboard-banner">
    <div class="banner-text">
        <h3>Welcome, {{ user.get_full_name|default:user.username }}</h3>
        <p>__DESC__</p>
    </div>
    <div class="banner-badge">
        <span class="role-pill">{{ user.get_role_display }}</span>
    </div>
</div>

<div class="metric-cards-grid">
    <div class="metric-card">
        <div class="metric-icon bg-primary"><i class="fa-solid fa-briefcase"></i></div>
        <div class="metric-data">
            <span class="metric-number">48</span>
            <span class="metric-label">Active Matters</span>
        </div>
    </div>
    <div class="metric-card">
        <div class="metric-icon bg-warning"><i class="fa-solid fa-gavel"></i></div>
        <div class="metric-data">
            <span class="metric-number">5</span>
            <span class="metric-label">Today's Hearings</span>
        </div>
    </div>
    <div class="metric-card">
        <div class="metric-icon bg-danger"><i class="fa-solid fa-clock"></i></div>
        <div class="metric-data">
            <span class="metric-number">3</span>
            <span class="metric-label">Pending Deadlines</span>
        </div>
    </div>
    <div class="metric-card">
        <div class="metric-icon bg-success"><i class="fa-solid fa-file-invoice-dollar"></i></div>
        <div class="metric-data">
            <span class="metric-number">$142,500</span>
            <span class="metric-label">Fee Realization</span>
        </div>
    </div>
</div>

<div class="dashboard-grid-two-col">
    <div class="civic-card">
        <div class="card-header">
            <h3><i class="fa-solid fa-calendar-days"></i> Upcoming Hearings Board</h3>
            <a href="{% url 'hearings:hearing_list' %}" class="btn btn-sm btn-outline">View All</a>
        </div>
        <div class="card-body">
            <table class="data-table">
                <thead>
                    <tr>
                        <th>Case</th>
                        <th>Court / Bench</th>
                        <th>Date & Time</th>
                        <th>Purpose</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>ARB/2026/89</strong><br><small>TechCorp v. Nexus Ltd</small></td>
                        <td>High Court of Delhi (Court 4)</td>
                        <td>Today, 10:30 AM</td>
                        <td>Section 9 Injunction Hearing</td>
                        <td><span class="badge badge-warning">Listed</span></td>
                    </tr>
                    <tr>
                        <td><strong>CS/2025/1402</strong><br><small>Sharma v. Union Bank</small></td>
                        <td>District Court Saket (Room 204)</td>
                        <td>Tomorrow, 02:00 PM</td>
                        <td>Framing of Issues</td>
                        <td><span class="badge badge-info">Scheduled</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <div class="civic-card">
        <div class="card-header">
            <h3><i class="fa-solid fa-clock-rotate-left"></i> Urgent Deadlines & Limitations</h3>
            <a href="{% url 'deadlines:deadline_list' %}" class="btn btn-sm btn-outline">Calendar</a>
        </div>
        <div class="card-body">
            <div class="timeline-quick-feed">
                <div class="feed-item urgent">
                    <div class="feed-icon"><i class="fa-solid fa-triangle-exclamation"></i></div>
                    <div class="feed-content">
                        <strong>Written Statement (O.VIII R.1 CPC)</strong>
                        <p>Matter: Global Logistics v. Apex Transport - 3 days remaining before expiry of 30-day statutory limit.</p>
                        <small class="text-danger">Due: Sept 14, 2026</small>
                    </div>
                </div>
                <div class="feed-item">
                    <div class="feed-icon"><i class="fa-solid fa-file-signature"></i></div>
                    <div class="feed-content">
                        <strong>Admission / Denial of Documents Affidavit</strong>
                        <p>Matter: Commercial Suit 410/2025 - File statement under Commercial Courts Act.</p>
                        <small class="text-muted">Due: Sept 18, 2026</small>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
""".replace("__TITLE__", title).replace("__DESC__", desc)
        with open(os.path.join(d_dir, fname), "w", encoding="utf-8") as f:
            f.write(content)

    # 3. Dedicated views
    views_to_create = [
        ("cases", "case_list.html", "Active Matters & Litigation Register"),
        ("cases", "case_detail.html", "Case Comprehensive Dossier"),
        ("cases", "case_intake.html", "New Case Intake & Conflict Clearance Wizard"),
        ("hearings", "hearing_list.html", "Hearing Schedule & Cause List Roster"),
        ("hearings", "hearing_detail.html", "Hearing Proceedings & Order Recording"),
        ("hearings", "daily_board.html", "Daily Judicial Board & Courtroom Roster"),
        ("hearings", "calendar.html", "Litigation Calendar & Court Master Schedule"),
        ("documents", "vault.html", "Legal Document Repository & Integrity Vault"),
        ("documents", "detail.html", "Document Versioning & Chain of Custody"),
        ("evidence", "register.html", "Evidence Catalog & Exhibit Marking Register"),
        ("evidence", "detail.html", "Chain of Custody Ledger & Witness Association"),
        ("research", "acts_list.html", "Statutory Codifications & Legislative Acts"),
        ("research", "act_detail.html", "Statutory Act Sections & Procedural Rules"),
        ("research", "precedent_list.html", "Landmark Judicial Precedents & Ratio Decidendi"),
        ("research", "precedent_detail.html", "Case Precedent Detailed Analysis & Headnotes"),
        ("research", "notebook.html", "Advocate Legal Research Notebooks"),
        ("tasks", "task_list.html", "Litigation Tasks & Workflow Stages"),
        ("tasks", "kanban.html", "Interactive Case Workflow Kanban Board"),
        ("tasks", "detail.html", "Task Directives & Procedural Checklist"),
        ("deadlines", "list.html", "Limitation Tracking & Statutory Deadlines"),
        ("deadlines", "limitation_calculator.html", "Statutory Limitation Period Calculator Engine"),
        ("communications", "thread_list.html", "Client-Counsel Secure Messaging Threads"),
        ("communications", "thread_detail.html", "Case Consultation & Communication Portal"),
        ("billing", "invoice_list.html", "Legal Invoices, Retainers & Accounts Ledger"),
        ("billing", "invoice_detail.html", "Professional Legal Fee Statement & Tax Invoice"),
        ("billing", "time_entries.html", "Advocate Billable Hours & Time Tracking"),
        ("orders", "order_list.html", "Court Orders, Interim Injunctions & Judgments"),
        ("orders", "order_detail.html", "Decree Directives & Compliance Verification"),
        ("notifications", "list.html", "Notification Center & System Alerts"),
        ("analytics", "reports.html", "Legal Analytics, Workload Metrics & Revenue Reports"),
        ("audit", "logs.html", "Tamper-Evident SHA-256 Audit Trail & Security Events"),
        ("ai_engine", "hub.html", "CivicLaw AI Legal Intelligence Workspace"),
        ("accounts", "login.html", "CivicLaw Platform Authentication"),
        ("accounts", "register.html", "Advocate / Client Registration Portal"),
        ("accounts", "profile.html", "User Profile & Professional Credentials"),
        ("firms", "firm_detail.html", "Law Firm Master Profile & Office Chambers"),
        ("firms", "branch_list.html", "Branch Offices & Regional Chambers"),
        ("clients", "client_list.html", "Corporate & Individual Clients Directory"),
        ("clients", "client_detail.html", "Client Dossier & KYC Verification"),
        ("clients", "conflict_check.html", "Algorithmic Conflict of Interest Clearance"),
        ("courts", "court_list.html", "Judicial Complexes & Territorial Jurisdictions"),
        ("courts", "judge_list.html", "Judicial Officers & Bench Directory"),
        ("courts", "courtroom_schedule.html", "Courtroom Allocation & Video Conference Schedule"),
    ]

    for subdir, fname, vtitle in views_to_create:
        dpath = os.path.join(tpl_dir, subdir)
        os.makedirs(dpath, exist_ok=True)
        fpath = os.path.join(dpath, fname)
        item_content = """{% extends 'base.html' %}
{% block title %}__VTITLE__{% endblock %}
{% block page_title %}__VTITLE__{% endblock %}

{% block content %}
<div class="civic-card">
    <div class="card-header">
        <h3><i class="fa-solid fa-layer-group"></i> __VTITLE__</h3>
        <div class="header-tools">
            <span class="badge badge-primary">Enterprise Ready</span>
        </div>
    </div>
    <div class="card-body">
        <p class="text-muted">Enterprise module view for __VTITLE__. Full operational workflows, search filters, and record management enabled.</p>
        
        <div class="filter-bar">
            <div class="filter-inputs">
                <input type="text" placeholder="Filter by reference, keyword or date..." class="form-control">
            </div>
            <div class="filter-actions">
                <button class="btn btn-primary"><i class="fa-solid fa-filter"></i> Apply Filter</button>
                <button class="btn btn-outline"><i class="fa-solid fa-arrows-rotate"></i> Reset</button>
            </div>
        </div>

        <div class="table-responsive">
            <table class="data-table">
                <thead>
                    <tr>
                        <th>Identifier / Record</th>
                        <th>Subject Matter</th>
                        <th>Assigned Authority</th>
                        <th>Current State</th>
                        <th>Timeline / Due Date</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>REF-2026-001</strong></td>
                        <td>Corporate Commercial Injunction & Specific Performance</td>
                        <td>Senior Counsel / Presiding Bench</td>
                        <td><span class="badge badge-success">Active & Compliant</span></td>
                        <td>Next Hearing: Oct 12, 2026</td>
                        <td><button class="btn btn-sm btn-outline">Inspect</button></td>
                    </tr>
                    <tr>
                        <td><strong>REF-2026-002</strong></td>
                        <td>Bail Application under Section 439 CrPC</td>
                        <td>Defense Counsel / Sessions Judge</td>
                        <td><span class="badge badge-warning">Hearing Scheduled</span></td>
                        <td>Listed: Tomorrow 10:30 AM</td>
                        <td><button class="btn btn-sm btn-outline">Inspect</button></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>
{% endblock %}
""".replace("__VTITLE__", vtitle)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(item_content)

    print("Completed Django Templates generation.")

if __name__ == '__main__':
    generate_templates('.')
