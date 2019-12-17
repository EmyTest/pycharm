'''批量合并'''


import os
from PyPDF2 import PdfFileReader, PdfFileWriter #导入需要的类（库）
wp='D:/temp_resource/pdf_practice/' #work_path

#合并同一个文件夹下的pdf文件
flst=[] #获得pdf文件路径
for root, dirs, files in os.walk(wp):
    flst=files
flst=[wp+f for f in flst]
out_pdf=PdfFileWriter()
for pf in flst:
    in_pdf=PdfFileReader(open(pf, 'rb')) #二进制打开
    page_count=in_pdf.getNumPages() #输入pdf的页数
    for pc in range(page_count):
        out_pdf.addPage(in_pdf.getPage(pc)) #逐页循环
with open(wp+'合并笔记_1-3章.pdf','wb') as wf:
    out_pdf.write(wf)
#out_pdf.getNumPages()