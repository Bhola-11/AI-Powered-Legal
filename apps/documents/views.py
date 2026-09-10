from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import LegalDocument, DocumentCategory

@login_required
def document_vault(request):
    docs = LegalDocument.objects.filter(is_deleted=False).select_related('case', 'category')
    if request.user.is_client():
        docs = docs.filter(is_client_visible=True)
    return render(request, 'documents/vault.html', {'documents': docs})

@login_required
def document_detail(request, pk):
    doc = get_object_or_404(LegalDocument, pk=pk)
    versions = doc.versions.all().order_by('-version_number')
    return render(request, 'documents/detail.html', {'document': doc, 'versions': versions})
