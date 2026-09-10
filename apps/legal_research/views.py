from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import StatutoryAct, StatutorySection, CasePrecedent, ResearchNotebook

@login_required
def acts_list(request):
    acts = StatutoryAct.objects.all().order_by('title')
    return render(request, 'research/acts_list.html', {'acts': acts})

@login_required
def act_detail(request, pk):
    act = get_object_or_404(StatutoryAct, pk=pk)
    sections = act.sections.all().order_by('id')
    return render(request, 'research/act_detail.html', {'act': act, 'sections': sections})

@login_required
def precedent_list(request):
    precedents = CasePrecedent.objects.all().order_by('-judgment_date')
    return render(request, 'research/precedent_list.html', {'precedents': precedents})

@login_required
def precedent_detail(request, pk):
    prec = get_object_or_404(CasePrecedent, pk=pk)
    return render(request, 'research/precedent_detail.html', {'precedent': prec})

@login_required
def notebook_view(request):
    notebooks = ResearchNotebook.objects.filter(author=request.user)
    return render(request, 'research/notebook.html', {'notebooks': notebooks})
