import os

from django.conf import settings

from .models import Document
from .utils import search_in_pdf_file, search_in_pptx_file


def search_in_docs(searched_data):
    matched_documents = []
    documents = Document.objects.all()
    for document in documents:
        if searched_data in document.document.name.split('/')[1].lower():
            matched_documents += [document]
            continue
        pdf_path = os.path.join(settings.MEDIA_ROOT, document.document.name)
        if pdf_path.endswith('.pdf'):
            search_in_file = search_in_pdf_file(pdf_path, searched_data)
            if search_in_file:
                matched_documents += [document]
                continue
        elif pdf_path.endswith('.pptx'):
            search_in_file = search_in_pptx_file(pdf_path, searched_data)
            if search_in_file:
                matched_documents += [document]
                continue
    return matched_documents
