import PyPDF2


with open('data.txt', 'a') as file:
    with open('data/data.pdf', 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)

        for page in reader.pages:
            file.write(page.extract_text())

        