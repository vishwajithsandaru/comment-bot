from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException as NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException as StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as opts
from json.decoder import JSONDecodeError as JSONDecodeError
from requests import get
from json import loads
from time import sleep

def init_fb():
    options = opts()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options = options, executable_path = './geckodriver')
    browser.get('https://www.facebook.com/navindu.vidanagama/posts/1465295743650296?__xts__[0]=68.ARArLYCmy8k0geBaE9THcZ_q-Eq0biyXd_4JrZIyUYZodrTSKzd-IePvJlFbBg9DmC1TC2U3eTRkvqhbvk3E_dVnNwExmbpUA_MZuKPt_pThqaKu0vawnfQFUo1ZXBOUHemVhCBZoUVWkZCNlUAFnlkyksrAGH1-TzyjkzGA1bQJw9kit_1tMFc1jl9L1TirsrXltkuxJJhBnZHME7j4JixDA2wkRas2RAP30IWsqdaKo3GSXn9mL0CnFAXrUHVgcVAlsoEy5QPbLQ8t3oOfeMtnp8hS3vd2ZIFTTWni9QT1pw5Bgmj7MGmTHAIhBKXVg8cQzC7cUxvQLdknnLu3ydBN&__tn__=-R')
    sleep(5)
    insert_cred(browser)
    click_comment(browser)
    for i in range(0, 10000):
        sleep(10)
        cmt = get_quote()
        insert_comment(browser, cmt)
        

    print("Finish")

def insert_cred(browser):
    try:
        uname = browser.find_element_by_xpath("//div[@class='_5jb4']//input")
        pword = browser.find_element_by_xpath("//div[@class='_5jb5']//input")
        uname.send_keys("sandarukasthoori@gmail.com")
        pword.send_keys("ET4ZOV)*2JF2PcE%EpaRXhC)g")
        loginbtn = browser.find_element_by_xpath("//div[@class='_70g9']//button")
        loginbtn.click()
    except NoSuchElementException:
        sleep(2)
        insert_cred(browser)

def click_comment(browser):
    try:
        print("OK.. Good to go.")
        comlink = browser.find_element_by_xpath("//a[@title='Leave a comment']")
        comlink.click()
        
       
    except NoSuchElementException:
        sleep(2)
        click_comment(browser)

def insert_comment(browser, comment):
    try:
        
        combox = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[4]/div[2]/div/div/div/div/div/form/div/div/div[2]/div")
        combox.send_keys(comment)
        combox.send_keys(Keys.RETURN)
    except NoSuchElementException:
        sleep(2)
        insert_comment(browser, comment)

def get_quote():
    comment = ""
    try:
        response = get('http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
        comment = '{quoteText}'.format(**loads(response.text))
    except JSONDecodeError:
        print('JSON Exception caught.')
        get_quote()
    return comment

init_fb()