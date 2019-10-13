# class that get the pdf from original recall website

# import library
import requests_html
import requests
import pdf_transfer




# method to get pdf
def get_pdf(title,link):

    session = requests_html.HTMLSession() # initiate request session

    r = session.get(link)
    file = r.html.xpath('//*[@id="slwp_ctl00_PlaceHolderMain_ctl02_ctl00"]/div/div/ul/li/div/div/a') # find pdf file through xpath
    link = list(file[0].absolute_links)[0] # get the link of the file
    pdf = requests.get(link, stream=True) # get pdf through the link
    save = './static/pdf/temp/'+title+'.pdf' # saving directory
    with open(save, 'wb') as fd: # write the pdf byte data into pdf
        for chunk in pdf.iter_content(200):
            fd.write(chunk)

    pdf_transfer.transfer(title) # change the pdf format through pdf_transfer class
    return title

if __name__ == '__main__':
    get_pdf()