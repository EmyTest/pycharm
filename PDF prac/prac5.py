'''旋转页面 '''

from PyPDF2 import PdfFileReader, PdfFileWriter

def rotate_pages(pdf_path):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(path)
    # 顺时针旋转90度
    page_1 = pdf_reader.getPage(0).rotateClockwise(90)
    pdf_writer.addPage(page_1)
    # 逆时针旋转90度
    page_2 = pdf_reader.getPage(1).rotateCounterClockwise(90)
    pdf_writer.addPage(page_2)
    # 在正常方向上添加一页
    pdf_writer.addPage(pdf_reader.getPage(2))

    with open('rotate_pages.pdf', 'wb') as fh:
        pdf_writer.write(fh)

if __name__ == "__main__":
    path = '新路径.pdf'
    rotate_pages(path)