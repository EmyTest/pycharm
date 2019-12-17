import PyPDF2
pdfFileObj = open('meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText()) #返回该页文本的字符串