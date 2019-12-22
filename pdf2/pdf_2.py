#!/user/bin/env python3
# -*- coding:utf-8 -*-

from PyPDF2 import PdfFileReader, PdfFileWriter

def add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out):
    """把水印添加到pdf中"""
    pdf_output = PdfFileWriter()
    input_stream = open(pdf_file_in, 'rb')
    pdf_input = PdfFileReader(input_stream,strict=False)

    # 获取PDF文件的页数
    pageNum = pdf_input.getNumPages()

    # 读入水印pdf文件
    pdf_watermark = PdfFileReader(open(pdf_file_mark, 'rb',),strict=False) #确定是否应该警告用户所有问题并且还会导致一些可纠正的问题致命。默认为True
    # 给每一页打水印
    for i in range(pageNum):
        page = pdf_input.getPage(i)
        page.mergePage(pdf_watermark.getPage(0))
        page.compressContentStreams()  # 压缩内容
        pdf_output.addPage(page)
    pdf_output.write(open(pdf_file_out, 'wb'))

if __name__ == '__main__':
    pdf_file_in = 'HTTP_1.pdf'
    pdf_file_out = 'HTTP1_12.pdf'
    pdf_file_mark = 'watermark.pdf'
    add_watermark(pdf_file_in, pdf_file_mark, pdf_file_out)
