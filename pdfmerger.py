import PyPDF2

pdffiles = ["1.pdf", "2.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdffiles:
    pdffiles = open(filename, 'rb')
    pdfreader = PyPDF2.PdfReader(pdffiles)
    merger.append(pdfreader)
pdffiles.close()
merger.write('merged.pdf')
