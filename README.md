# PDFreeFlow

This is a simple Flask web application that allows users to upload a password-protected PDF file and remove the password protection by entering the password.

When a user submits the form, the web application uses the PyPDF2 library to open the uploaded PDF file and attempt to decrypt it with the entered password. If the decryption is successful, the application creates a new PDF file that contains all the pages from the original file but without the password protection. The unprotected PDF file is then returned to the user as a download.

The code is structured as follows:

The Flask application is created and a route is defined for the "/" URL.
The index function is called when the "/" URL is accessed using the POST method.
The uploaded PDF file is retrieved from the request object and opened using the PyPDF2 library.
The entered password is obtained from the request form and used to attempt to decrypt the PDF file.
If the decryption is successful, a new PDF file is created using PyPDF2 and all the pages from the original PDF file are added to it.
The new PDF file is saved and returned to the user as a download.
If the request method is not POST (i.e., the user is accessing the URL for the first time), the index function returns an HTML template.
