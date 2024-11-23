from .models import Document

def save_file(file):
    """
    Saves a file to the document storage if it has a valid extension.

    Args:
        file (File): The file object to be saved.

    Returns:
        dict: A dictionary containing a message indicating the success or failure of the file save operation.
    """
    message = {"message": "Document Was Saved Successfully"}
    document_file_extension = file.name
    if document_file_extension.endswith('.pptx') or document_file_extension.endswith('.pdf'):
        Document.objects.create(document=file)
    else:
        message["message"] = "Sorry, Files with extension .pdf,pptx only Allowed to Upload"
        message['error'] = True
    return message