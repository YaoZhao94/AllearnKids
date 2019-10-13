# class that handles get recall news from website, change format and store into databse

# import library
import xml.etree.ElementTree as ET
import requests
import pandas
import records
import notice
import time_zone
import time

# connect to database
db = records.Database('mysql://root:ECC12345$@mydatabase.cn2pbhimebqz.ap-southeast-2.rds.amazonaws.com/food_recall?charset=utf8')


# get the xml file and parse file to small pieces and write into dataframe
def xml_parse():
    # get xml file
    r = requests.get(
        'http://www.foodstandards.gov.au/_layouts/15/feed.aspx?xsl=1&web=/industry/foodrecalls/recalls&page=84343ba1-f84d-4c03-a936-400c17938b62&wp=9261fa06-60e7-425d-86bf-da2de3e26962&pageurl=/industry/foodrecalls/recalls/Pages/RSS.aspx')
    tree = ET.fromstring(r.text)

    title = []
    description = []
    link = []
    date = []

    # parse xml file
    for x in tree.findall('channel'):
        for y in x.findall('item'):
            for z in y.findall('title'):
                title.append(z.text)
            for a in y.findall('description'):
                description.append(a.text)
            for b in y.findall('link'):
                link.append(b.text)
            for c in y.findall('pubDate'):
                date.append(c.text)

    # write xml file into dataframe
    df = pandas.DataFrame()
    df['title'] = title
    df['description'] = description
    df['link'] = link
    df['date'] = date


    return (df)


# function that handles inserting data into database
def database_insert(data):
    dataframe = data
    print (dataframe)
    for index, x in dataframe.iterrows():
        # get the pdf file
        print ("index",index)
        pdf = notice.get_pdf(x['title'], x['link']) + ".pdf"

        # change time zone and format
        mel_time = time_zone.zone_change(x['date'])
        # insert the data into database

        query = "INSERT INTO recall(title,description,link,date,pdf,mel_time) VALUES (\"" + x['title'] + "\",\"" + x['description'] + "\",\"" + x['link'] + "\",\"" + x['date'] + "\",\"" + pdf + "\",\"" + mel_time + "\");"
        print (query)

        row = db.query(query)

        time.sleep(45)




new_entry = False
# function to check if there is a new entry and add into database
def check_new():
    global new_entry
    new_entry = False

    # initiate dataframe and get xml file
    df = pandas.DataFrame(columns = ['title','description','link','date'])
    dataframe = xml_parse()
    entry = db.query("SELECT * FROM recall ORDER BY id DESC LIMIT 1;") # get the latest entry

    # if the database is not empty
    if len(entry.all()) != 0:

        for index, x in dataframe.iterrows():

            if x['title'] != entry[0].title:
                df.loc[index] = x
            else:
                break
    else:
        df = dataframe.iloc[::-1]


    print (str(len(df))+" new entries")

    # add entry to database
    if len(df) != 0:
        new_entry = True
        database_insert(df)
        print (len(df)," entries add to database")
        return (True)
    else:
        return (False)


if __name__ == '__main__':
    check_new()
