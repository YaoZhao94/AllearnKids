import schedule
import time
import xml_parse


def daily():
    print ('running')
    xml_data = schedule.every().day.at("00:43").do(xml_parse.check_new)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    daily()