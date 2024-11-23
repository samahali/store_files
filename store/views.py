from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .selectores import search_in_docs
from .services import save_file

@require_http_methods(["GET"])
def upload_files_page(request):
    """
    Renders the file upload page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page for file upload.
    """
    return render(request, template_name="store/upload_files.html")

@require_http_methods(["POST"])
def search_in_files(request):
    """
    Searches for specific data in uploaded documents.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML page with matched documents or a JSON response with an error message.
    """
    try:
        searched_data =request.POST["search_file"].lower()
        matched_documents= search_in_docs(searched_data)
        if matched_documents:
            return render(
                request,
                template_name="store/matched_documents.html",
                context={"documents": matched_documents}
            )
        else:
            return JsonResponse({
                "error":True,"message":"No items match your search."
            })
    except Exception as e:
        return JsonResponse({
            "error":True,
            "message":"an application error has occurred, please contact your administrator."
        })

@require_http_methods(["POST"])
def add_file(request):
    """
    Adds a new file to the document storage.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response indicating the success or failure of the file upload.
    """
    try:
        document_file = request.FILES["uploadedFile"]
        message = save_file(document_file)
        return JsonResponse(message)
    except Exception as e:
        return JsonResponse({
            "error":True,
            "message":"an application error has occurred, please contact your administrator."
        })
