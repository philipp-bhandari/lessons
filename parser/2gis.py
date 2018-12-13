from selenium import webdriver
from selenium.webdriver import FirefoxOptions
import time
import gc
import logging
import os
from bs4 import BeautifulSoup
from pprint import pprint


def setup_logging():
    logging.basicConfig(format='[%(asctime)s] %(levelname).1s %(message)s',
                        filename='./parser_2gis.log',
                        datefmt='%Y.%m.%d %H:%M:%S',
                        level=logging.INFO)


def main():
    browser = None
    try:
        logging.info("starting browser")
        OPTIONS = FirefoxOptions()
        #OPTIONS.add_argument("--headless")
        load_timeout = 1000
        browser = webdriver.Firefox(firefox_options=OPTIONS)
        browser.set_page_load_timeout(load_timeout)
        if os.path.exists('./accounting'):
            # urls = []
            with open("./accounting", "r") as file:
                urls = [row.strip() for row in file]
            time.sleep(1)
            title = "h1[class=\"cardHeader__headerNameText\"]"
            phone = "a[class=\"contact__phonesItemLink\"]"
            all_contacts = "div[class=\"contact__link _type_email\"]"


            with open("./result.csv", "a") as file:
                for index, url in enumerate(urls):
                    try:
                        browser.get(url)
                        time.sleep(1)
                        # name = browser.find_element_by_css_selector(title).text
                        # contact = browser.find_element_by_css_selector(phone).get_attribute('href')[5:]
                        results = browser.page_source

                        soup = BeautifulSoup(results, 'html.parser')
                        name = soup.select(title)[0].string
                        contact = soup.select(phone)[0].string
                        try:
                            email = soup.select(all_contacts)[0].string
                        except:
                            email = ''

                        file.write("{};{};{}\n".format(name, contact, email))
                        file.flush()
                        del name
                        del contact
                        del soup
                        del results
                        gc.collect()
                    except:
                        logging.exception(Exception)
        else:
            css_selector_url = "h3[class=\"miniCard__headerTitle\"]"
            urls = []
            for i in range(1, 100):
                url = "https://2gis.ru/moscow/search/%D1%85%D0%BE%D1%81%D1%82%D0%B5%D0%BB%D1%8B/page/{}?queryState=center%2F37.619591%2C55.753202%2Fzoom%2F11".format(i)
                browser.get(url)
                time.sleep(1)
                try:
                    results = browser.page_source
                    soup = BeautifulSoup(results, 'html.parser')
                    h3_objects = soup.select(css_selector_url)
                    for h3 in h3_objects:
                        urls.append("https://2gis.ru{}".format(h3.contents[0].attrs['href']))
                except:
                    logging.exception(Exception)

                gc.collect()
            time.sleep(1)
            with open("./accounting", "w") as file:
                for ref in urls:
                    file.write("{}\n".format(ref))
    finally:
        if browser:
            browser.quit()
            logging.info("Closing browser")


if __name__ == '__main__':
    setup_logging()
    main()
