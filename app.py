from flask import Flask, request, render_template, send_file
import PyPDF2
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the uploaded PDF file
        pdf_file = request.files["pdf_file"]

        # Open the PDF file in read-only mode
        pdf_reader = PyPDF2.PdfReader(pdf_file.stream)

        # Enter the password for the PDF file
        password = request.form["password"]
        pdf_reader.decrypt(password)

        # Create a new PDF file to store the unprotected version
        pdf_writer = PyPDF2.PdfWriter()

        # Add all the pages from the original PDF file to the new one
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

        # Save the new PDF file
        unprotected_pdf = open("unprotected.pdf", "wb")
        pdf_writer.write(unprotected_pdf)

        # Close the PDF files
        unprotected_pdf.close()

        # Return the unprotected PDF file to the user
        return send_file("unprotected.pdf", as_attachment=True)

    return render_template("index.html")

port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    app.run(port=port)
