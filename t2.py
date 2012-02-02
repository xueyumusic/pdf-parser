
import sys
import StringIO
from pdfminer.pdfparser import PDFDocument, PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, process_pdf
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams

outtype = "txt"
outfile = "pdf2.txt"
codec = 'utf-8'
args = ['m2.pdf']

rsrc = PDFResourceManager()
outfp = file(outfile, 'w')
device = TextConverter(rsrc, outfp, codec=codec, laparams=None)
for fname in args:
        fp = file(fname, 'rb')
        process_pdf(rsrc, device, fp, None, maxpages=0, password='')
        fp.close()
device.close()
outfp.close() 

