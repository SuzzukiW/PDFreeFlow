from flask import Flask, request, render_template, send_file
import PyPDF2
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the uploaded PDF file
        pdf_file = request.files.get("pdf_file")
        if not pdf_file:
            return "No PDF file uploaded."

        # Open the PDF file in read-only mode
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file.stream)
        except Exception as e:
            return f"Error opening PDF file: {e}"

        # Check if the PDF file has any security restrictions
        if pdf_reader.isEncrypted:
            # Enter the password for the PDF file
            password = request.form.get("password")
            if not password:
                return "No password entered."

            try:
                pdf_reader.decrypt(password)
            except Exception as e:
                return "Wrong password. This program cannot help you if you do not have the correct password for your PDF file."

        # Create a new PDF file to store the unprotected version
        pdf_writer = PyPDF2.PdfWriter()

        # Add all the pages from the original PDF file to the new one
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # Save the new PDF file
        try:
            with open("unprotected.pdf", "wb") as unprotected_pdf:
                pdf_writer.write(unprotected_pdf)
        except Exception as e:
            return f"Error saving unprotected PDF file: {e}"

        # Return the unprotected PDF file to the user
        return send_file("unprotected.pdf", as_attachment=True)

    return render_template("index.html")

port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(port=port)
