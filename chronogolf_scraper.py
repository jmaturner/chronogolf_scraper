import argparse
from selenium import webdriver
import email_results
import sys
import time

#this URL will be modified by the commandline args: date etc


def main(date):
    if not date:
        parser.error('date argument is required')
    url = f'https://www.chronogolf.com/club/langdon-farms-golf-club#?course_id=13667&nb_holes=18&date={date}&affiliation_type_ids=48570,48570'
    scrape(url)


def scrape(url):
    '''sets chrome options, launches browser and scrapes results'''
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome('/home/turner/selen_scrape/selen-env/bin/chromedriver91',options=options)
    driver.get(url)
    click_book = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]').click()
    time.sleep(2)
    times = driver.find_element_by_class_name("widget-teetimes").text
    driver.quit()
    print(times)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('date', help="date for golf '2021-07-04'",type=str)
    args = parser.parse_args()
    date = args.date
    main(date)


