from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .services import LegalAIService

@login_required
def ai_hub_view(request):
    summary_result = None
    draft_result = None
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'summarize':
            title = request.POST.get('title', 'Commercial Dispute')
            desc = request.POST.get('description', '')
            issues = request.POST.get('legal_issues', '')
            summary_result = LegalAIService.generate_case_summary(title, desc, issues)
        elif action == 'draft':
            ptype = request.POST.get('petition_type', 'Civil Plaint')
            cname = request.POST.get('client_name', 'M/s ABC Enterprises')
            oparty = request.POST.get('opposite_party', 'XYZ Corporation')
            relief = request.POST.get('relief_sought', 'Permanent Injunction')
            grounds = request.POST.get('grounds', '')
            draft_result = LegalAIService.draft_petition(ptype, cname, oparty, relief, grounds)
    return render(request, 'ai_engine/hub.html', {
        'summary_result': summary_result,
        'draft_result': draft_result,
    })
