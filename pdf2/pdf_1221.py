
# # encoding='utf-8'
# pdfFileObj = open('meetingminutes.pdf','rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
# pageObj = pdfReader.getPage(0)
# print(pageObj.extractText())

'''加密'''
# pdfFile = open('meetingminutes.pdf', 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFile)
# pdfWriter = PyPDF2.PdfFileWriter()
# for pageNum in range(pdfReader.numPages):
#     pdfWriter.addPage(pdfReader.getPage(pageNum))
#     pdfWriter.encrypt('password')
#     resultPdf = open('encryptmeeting.pdf', 'wb')
#     pdfWriter.write(resultPdf)
#     resultPdf.close()


'''接密'''
# pdfReader = PyPDF2.PdfFileReader(open('encryptmeeting.pdf','rb'))
# # print(pdfReader.isEncrypted)
# # pdfReader.getPage(0)   #报错
# pdfReader.decrypt('password')
# pageObj = pdfReader.getPage(0)
# print(pageObj)
# print(pageObj.extractText())

'''批量合并'''
import PyPDF2
from PyPDF2 import PdfFileReader,PdfFileWriter
# import os
#
# wp='D:/temp_resource/pdf_practice/' #work_path
#
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
# with open(wp+'combine.pdf','wb') as wf:
#     out_pdf.write(wf)
#     out_pdf.getNumPages()






#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
# def split(path, name_of_split):
#     pdf = PdfFileReader(path)
#     for page in range(0,pdf.getNumPages()-1):
#         pdf_writer = PdfFileWriter()
#         pdf_writer.addPage(pdf.getPage(page))
#         output = f'{name_of_split}{page}.pdf'
#         with open(output, 'wb') as output_pdf:
#             pdf_writer.write(output_pdf)
# if __name__ == '__main__':
#     path = 'D:/temp_resource/pdf_practice/combine.pdf'
#     split(path, 'split_p')

import PyPDF2



import PyPDF2
minutesFile = open('meetingminutes.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(minutesFile)
minutesFirstPage = pdfReader.getPage(0)   #
pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))  #在minutesFirstPage 上调用mergePage()。传递给mergePage()  的参数，是 watermark.pdf 第一页的 Page 对象
pdfWriter = PyPDF2.PdfFileWriter()
pdfWriter.addPage(minutesFirstPage)
for pageNum in range(1,pdfReader.numPages):    #循环遍历 meetingminutes.pdf 的剩余页面，将它们添加到 PdfFileWriter 对象中
    pageObj = pdfReader.getPage(pageNum)
    pdfWriter.addPage(pageObj)
resultPdfFile = open('watermarkedCover.pdf','wb')
pdfWriter.write(resultPdfFile)
minutesFile.close()
resultPdfFile.close()






from PyPDF2 import PdfFileReader, PdfFileWriter

def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    """把水印添加到pdf中"""
    pdf_output = PdfFileWriter()
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfFileReader(input_stream, strict=False)

    # 获取PDF文件的页数
    pageNum = pdf_input.getNumPages()

    # 读入水印pdf文件
    pdf_watermark = PdfFileReader(open(pdf_file_mark, 'rb'), strict=False)
    # 给每一页打水印
    for i in range(pageNum):
        page = pdf_input.getPage(i)
        page.mergePage(pdf_watermark.getPage(0))
        page.compressContentStreams()  # 压缩内容
        pdf_output.addPage(page)
    pdf_output.write(open(pdf_file_out, 'wb'))

if __name__ == '__main__':
    pdf_file_in = 'soapUI_st.pdf'
    pdf_file_out = 'soapwatermark.pdf'
    pdf_file_mark = 'watermark.pdf'
    add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)









