from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

driver = webdriver.Chrome(executable_path=r"C:\Program Files (x86)\ChromeDriver\chromedriver.exe")
driver.get('https://www.youtube.com/')

element = driver.find_element_by_name("search_query")
element.send_keys('Pewdipie', Keys.ENTER)

# driver.find_element_by_xpath('//*[@id="avatar-section"]/a').click()
driver.find_element_by_tag_name('ytd-channel-renderer').click()

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="tabsContent"]/paper-tab[2]')))

driver.find_element_by_xpath('//*[@id="tabsContent"]/paper-tab[2]').click()

sleep(3)


def scrolDown():
    run = True
    dom = driver.find_element_by_tag_name('body')
    i = 0
    while run:
        dom.send_keys(Keys.PAGE_DOWN)
        i = i + 1
        if i == 20:
            run = False


def selectItem():
    items = driver.find_elements_by_tag_name('ytd-grid-video-renderer')
    names = []
    for item in items:
        video_name = item.find_element_by_id('video-title')
        names.append(video_name)

    selected = random.randint(0, len(names))
    print(selected)
    #items[selected].click()
    webdriver.ActionChains(driver).move_to_element(items[selected]).click(items[selected]).perform()


scrolDown()
sleep(2)
selectItem()
