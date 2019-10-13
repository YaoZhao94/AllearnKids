# class that transfer pdf to format that can store in ELB

# import library
from pdf2jpg import pdf2jpg
import os

# transfer function
def transfer(title):
    #set path
    inputpath = r"./static/pdf/temp/" + title + ".pdf"
    outputpath = r"./static/pdf/" + title +".pdf"
    try:
        # try if can transfer to pdf image
        result = pdf2jpg.convert_pdf2imgpdf(inputpath, outputpath, dpi=50)
        os.remove(inputpath)
        print (title + "has removed")
    except:
        # if not, print error
        print ("problem happened")