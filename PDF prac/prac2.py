'''加密'''
import PyPDF2

pdffile1= open('meetingminutes.pdf','rb')

pdf_reader1= PyPDF2.PdfFileReader(pdffile1)

# 将读取的内容写入对象中

pdfwriter= PyPDF2.PdfFileWriter()

for pagenum in range(pdf_reader1.numPages):
    pdfwriter.addPage(pdf_reader1.getPage(pagenum))

# 输入口令

pdfwriter.encrypt('meimei')

# # 真正创建PDF文件
#
# result_pdf= open('meeting222.pdf','wb')
#
# pdfwriter.write(result_pdf)
#
# # 关闭文件

