import PyPDF2
import os
merger = PyPDF2.PdfMerger() 

for file in os.listdir(os.getcwd()):
    if file.endswith(".pdf"):
        merger.append(file)  

merger.write("result.pdf")
merger.close()

print("PDFs merged successfully into 'result.pdf'")