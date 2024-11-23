from django.urls import path
from store.views import search_in_files, add_file, upload_files_page

app_name="store"

urlpatterns = [
    path('files/', upload_files_page, name ="files_management"),
    path('search/', search_in_files,name = "search"),
    path('add-file/', add_file, name="add_file"),
]