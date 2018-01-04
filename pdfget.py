import os
from PyPDF2 import PdfFileReader

path = "/home/cameryn/projects/realpython1/sample_files"

input_file_name = os.path.join(path, "1342-pdf.pdf")
input_file = PdfFileReader(open(input_file_name, "rb"))

print("Number of pages:", input_file.getNumPages())
print("Title:", input_file.getDocumentInfo().title)
