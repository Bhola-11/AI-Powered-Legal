// CivicLaw Enterprise Interactive Client Module
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
