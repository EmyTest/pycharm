'''解密'''
import PyPDF2



pdfReader = PyPDF2.PdfFileReader(open('meetingminutes.pdf','rb'))
# print(pdfReader.isEncrypted)
# pdfReader.getPage(0)   #报错
pdfReader.decrypt('swordfish')
pageObj = pdfReader.getPage(2)
# print(pageObj)
print(pageObj.extractText())

#
# pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf','rb'))
# # print(pdfReader.isEncrypted)
# # pdfReader.getPage(0)   #报错
# pdfReader.decrypt('rosebud')
# pageObj = pdfReader.getPage(2)
# # print(pageObj)
# print(pageObj.extractText())