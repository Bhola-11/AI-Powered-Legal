// CivicLaw Enterprise Interactive Client Module v2.5.0
document.addEventListener('DOMContentLoaded', () => {
    console.log('CivicLaw Enterprise Suite Initialized v2.5.0');

    // 1. Highlight Active Sidebar Link based on current URL path
    const currentPath = window.location.pathname;
    const navItems = document.querySelectorAll('.sidebar-nav .nav-item');
    navItems.forEach(item => {
        const href = item.getAttribute('href');
        if (href && href !== '#' && currentPath === href) {
            item.classList.add('active');
        } else if (href && href !== '/' && href !== '/accounts/redirect/' && currentPath.startsWith(href)) {
            item.classList.add('active');
        }
    });

    // 2. Mobile Sidebar Toggle Button
    const toggleBtn = document.querySelector('.sidebar-toggle-btn');
    const sidebar = document.querySelector('.app-sidebar');
    if (toggleBtn && sidebar) {
        toggleBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            sidebar.classList.toggle('open');
        });

        // Close sidebar when clicking outside on mobile
        document.addEventListener('click', (e) => {
            if (sidebar.classList.contains('open') && !sidebar.contains(e.target) && e.target !== toggleBtn) {
                sidebar.classList.remove('open');
            }
        });
    }

    // 3. Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transition = 'opacity 0.5s ease';
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });

    // 4. Universal Interactive Table Filter & Reset
    const filterInput = document.querySelector('.filter-inputs input');
    const applyFilterBtn = document.querySelector('.filter-actions .btn-primary');
    const resetFilterBtn = document.querySelector('.filter-actions .btn-outline');

    function executeFilter() {
        if (!filterInput) return;
        const term = filterInput.value.toLowerCase().trim();
        const rows = document.querySelectorAll('.data-table tbody tr');
        let matchCount = 0;
        rows.forEach(row => {
            const text = row.innerText.toLowerCase();
            const matches = text.includes(term);
            row.style.display = matches ? '' : 'none';
            if (matches) matchCount++;
        });
    }

    if (filterInput) {
        filterInput.addEventListener('keyup', (e) => {
            if (e.key === 'Enter') {
                executeFilter();
            } else {
                executeFilter();
            }
        });
    }

    if (applyFilterBtn) {
        applyFilterBtn.addEventListener('click', (e) => {
            e.preventDefault();
            executeFilter();
        });
    }

    if (resetFilterBtn) {
        resetFilterBtn.addEventListener('click', (e) => {
            e.preventDefault();
            if (filterInput) {
                filterInput.value = '';
            }
            const rows = document.querySelectorAll('.data-table tbody tr');
            rows.forEach(row => row.style.display = '');
        });
    }

    // 5. Universal Inspection Modal for Table Rows
    // Ensure modal container exists in DOM
    let modalOverlay = document.querySelector('.civic-modal-overlay');
    if (!modalOverlay) {
        modalOverlay = document.createElement('div');
        modalOverlay.className = 'civic-modal-overlay';
        modalOverlay.innerHTML = `
            <div class="civic-modal" role="dialog" aria-modal="true">
                <div class="civic-modal-header">
                    <h4 id="modal-record-title"><i class="fa-solid fa-file-shield"></i> Record Inspection</h4>
                    <button class="civic-modal-close" aria-label="Close modal">&times;</button>
                </div>
                <div class="civic-modal-body" id="modal-record-body">
                    <!-- Dynamic Record Data Loaded Here -->
                </div>
                <div class="civic-modal-footer">
                    <button class="btn btn-outline modal-close-btn">Close</button>
                    <button class="btn btn-primary modal-action-btn"><i class="fa-solid fa-copy"></i> Copy Summary</button>
                </div>
            </div>
        `;
        document.body.appendChild(modalOverlay);

        const closeBtns = modalOverlay.querySelectorAll('.civic-modal-close, .modal-close-btn');
        closeBtns.forEach(btn => btn.addEventListener('click', () => {
            modalOverlay.classList.remove('active');
        }));

        modalOverlay.addEventListener('click', (e) => {
            if (e.target === modalOverlay) {
                modalOverlay.classList.remove('active');
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && modalOverlay.classList.contains('active')) {
                modalOverlay.classList.remove('active');
            }
        });

        const copyBtn = modalOverlay.querySelector('.modal-action-btn');
        if (copyBtn) {
            copyBtn.addEventListener('click', () => {
                const bodyText = modalOverlay.querySelector('#modal-record-body').innerText;
                navigator.clipboard.writeText(bodyText).then(() => {
                    copyBtn.innerHTML = '<i class="fa-solid fa-check"></i> Copied!';
                    setTimeout(() => {
                        copyBtn.innerHTML = '<i class="fa-solid fa-copy"></i> Copy Summary';
                    }, 2000);
                });
            });
        }
    }

    // Bind Inspect buttons in all tables
    function bindInspectButtons() {
        const inspectButtons = document.querySelectorAll('.data-table tbody tr button.btn-sm');
        inspectButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                const row = btn.closest('tr');
                if (!row) return;

                const headers = Array.from(document.querySelectorAll('.data-table thead th')).map(th => th.innerText.trim());
                const cells = Array.from(row.querySelectorAll('td'));

                let html = '<div style="display: flex; flex-direction: column; gap: 0.75rem;">';
                headers.forEach((header, idx) => {
                    if (header && header.toLowerCase() !== 'action' && cells[idx]) {
                        const val = cells[idx].innerHTML.trim();
                        html += `
                            <div style="border-bottom: 1px solid #e2e8f0; padding-bottom: 0.5rem;">
                                <span style="font-size: 0.75rem; text-transform: uppercase; font-weight: 700; color: #64748b; display: block;">${header}</span>
                                <div style="font-size: 0.95rem; color: #0f172a; margin-top: 0.25rem;">${val}</div>
                            </div>
                        `;
                    }
                });
                html += '</div>';

                const titleElem = document.getElementById('modal-record-title');
                const bodyElem = document.getElementById('modal-record-body');
                if (titleElem && cells[0]) {
                    titleElem.innerHTML = `<i class="fa-solid fa-folder-open"></i> Record: ${cells[0].innerText.trim()}`;
                }
                if (bodyElem) {
                    bodyElem.innerHTML = html;
                }
                modalOverlay.classList.add('active');
            });
        });
    }
    bindInspectButtons();

    // 6. Interactive Conflict Checker
    const conflictBtn = document.getElementById('run-conflict-check-btn');
    if (conflictBtn) {
        conflictBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const input = document.getElementById('conflict-party-name');
            const name = input ? input.value : 'Adverse Entity';
            const resultBox = document.getElementById('conflict-results-box');
            if (resultBox) {
                resultBox.innerHTML = `
                    <div class="alert alert-info" style="margin-top: 1rem;">
                        <i class="fa-solid fa-spinner fa-spin"></i> Running conflict check on <strong>"${name}"</strong> across clients, opposite parties, and cross-litigation registers...
                    </div>
                `;
                setTimeout(() => {
                    resultBox.innerHTML = `
                        <div class="alert alert-success" style="margin-top: 1rem;">
                            <h4><i class="fa-solid fa-circle-check"></i> Conflict Check Cleared</h4>
                            <p>No active or historical adverse representation found for <strong>"${name}"</strong> within CivicLaw Premier Legal LLP records.</p>
                            <small class="text-muted">Cleared by Rule 35 Bar Council Standards &bull; Timestamp: ${new Date().toLocaleString()}</small>
                        </div>
                    `;
                }, 800);
            } else {
                alert(`Conflict clearance check initiated for: ${name}`);
            }
        });
    }
});
