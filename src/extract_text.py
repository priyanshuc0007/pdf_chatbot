from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

if __name__ == "__main__":
    pdf_text = extract_text_from_pdf(r"data\thehindu.pdf")
    print(pdf_text[:500])  # Print first 500 characters for verification
