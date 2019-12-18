'''
-- 从Python中提取PDF中的文档信息
-- 旋转页面
-- 合并PDF
-- 拆分PDF
-- 加水印
-- 加密PDF
'''


'''从Python中提取PDF中的文档信息'''
# import PyPDF2
# from PyPDF2 import PdfFileReader
#
# def extract_information(pdf_path):
#     with open(pdf_path, 'rb') as f:
#         pdf = PdfFileReader(f)
#         information = pdf.getDocumentInfo()
#         number_of_pages = pdf.getNumPages()
#
#     txt = f"""
#     Information about {pdf_path}:
#
#     Author: {information.author}
#     Creator: {information.creator}
#     Producer: {information.producer}
#     Subject: {information.subject}
#     Title: {information.title}
#     Number of pages: {number_of_pages}
#     """
#
#     print(txt)
#     return information
#
# if __name__ == '__main__':
#     path = 'D:/temp_resource/pdf_practice/Python_auto.pdf'
#     extract_information(path)


'''旋转页面'''

# import PyPDF2
# minutesFile = open('D:/temp_resource/pdf_practice/p1.pdf','rb')
# pdfReader = PyPDF2.PdfFileReader(minutesFile)
# page = pdfReader.getPage(0) #选择PDF第一页
# page.rotateClockwise(90)
# pdfWriter = PyPDF2.PdfFileWriter()
# pdfWriter.addPage(page)
# resultPdfFile = open('rotatedPage.pdf','wb') #旋转90°，保存成一个新文档
# pdfWriter.write(resultPdfFile)
# resultPdfFile.close()
# minutesFile.close()

'''合并PDF'''
#
# import os
# from PyPDF2 import PdfFileReader, PdfFileWriter #导入需要的类（库）
# wp='D:/temp_resource/pdf_practice/' #work_path
#
# #合并同一个文件夹下的pdf文件
# flst=[] #获得pdf文件路径
# for root, dirs, files in os.walk(wp):
#     flst=files
# flst=[wp+f for f in flst]
# out_pdf=PdfFileWriter()
# for pf in flst:
#     in_pdf=PdfFileReader(open(pf, 'rb')) #二进制打开
#     page_count=in_pdf.getNumPages() #输入pdf的页数
#     for pc in range(page_count):
#         out_pdf.addPage(in_pdf.getPage(pc)) #逐页循环
# with open(wp+'合并笔记_1-3.pdf','wb') as wf:
#     out_pdf.write(wf)
# #out_pdf.getNumPages()



'''拆分PDF'''

from PyPDF2 import PdfFileReader, PdfFileWriter

def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)

if __name__ == '__main__':
    path = 'D:/temp_resource/pdf_practice/HTTP authority Guide.pdf'
    split(path, 'jupyter_page')







'''加水印'''
#
# import PyPDF2
# minutesFile = open('D:/temp_resource/pdf_practice/p2.pdf','rb')
# pdfReader = PyPDF2.PdfFileReader(minutesFile)
# minutesFirstPage = pdfReader.getPage(0)   #
# pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
# minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))  #在minutesFirstPage 上调用mergePage()。传递给mergePage()
#                                                             # 的参数，是 watermark.pdf 第一页的 Page 对象
# pdfWriter = PyPDF2.PdfFileWriter()
# pdfWriter.addPage(minutesFirstPage)
#
# for pageNum in range(1,pdfReader.numPages):    #循环遍历 meetingminutes.pdf 的剩余页面，将它们添加到 PdfFileWriter 对象中
#     pageObj = pdfReader.getPage(pageNum)
#     pdfWriter.addPage(pageObj)
# resultPdfFile = open('watermarkedCover.pdf','wb')
# pdfWriter.write(resultPdfFile)
# minutesFile.close()
# resultPdfFile.close()

#test111