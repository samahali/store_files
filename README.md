## Django File Upload App
### Overview
This Django app allows users to upload files with extensions .pdf and .pptx. It provides functionality to save the uploaded files and search for specific data within these files.

#### Features
* File Upload: Users can upload .pdf and .pptx files.

* File Search: Users can search for specific data within the uploaded files.

* File Management: A simple interface to manage uploaded files.

#### Installation
    git clone <repository_url>
---
    cd <repository_directory>
---
    docker compose up --build

#### Usage
###### Uploading Files
* Navigate to the file upload page.

* Select the file you want to upload.

* Click the upload button.

* Searching for Data in Files
* Enter the data you want to search for in the input field. 
* Click the search button.

###### Configuration
* Allowed File Extensions: The app currently allows only .pdf and .pptx files to be uploaded. You can modify this in the save_file function.
* File Storage: By default, files are saved in the database. You can configure this to use a different storage backend if needed.

