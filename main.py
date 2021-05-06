from selenium import webdriver
import time
import numpy as np
from selenium.webdriver.chrome.options import Options

option = Options()
#option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])
option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.3")
browser = webdriver.Chrome(options=option)

#Посилання на саму форму
url = "https://docs.google.com/forms/d/e/1FAIpQLScDRtRlKTc0qj57jpiZS37Sd2wR2sxptx4aQ6QWV0vW2dUhdA/viewform"
#Твій ПІБ
your_name = "Фем'як Михайло Миколайович"

browser.get(url)
time.sleep(1)
name = browser.find_element_by_xpath("//input[@type='text']")
name.send_keys(your_name)
next_button = browser.find_element_by_xpath("//span[@class='appsMaterialWizButtonPaperbuttonContent exportButtonContent']")
next_button.click()

###############################################################
arr_question = browser.find_elements_by_class_name("freebirdFormviewerComponentsQuestionRadioChoicesContainer")

answ = []
while len(answ) < len(arr_question):
    answ.append(0)

max_count_answ = 0
for count in arr_question:
    if(max_count_answ < len(count.find_elements_by_class_name("docssharedWizToggleLabeledContainer"))):
        max_count_answ = len(count.find_elements_by_class_name("docssharedWizToggleLabeledContainer"))
submitt_button = browser.find_element_by_class_name('freebirdFormviewerViewNavigationSubmitButton')

to_max_count = int(0)
browser.close()
while to_max_count < max_count_answ:
    browser1 = webdriver.Chrome(options=option)
    browser1.get(url)
    name = browser1.find_element_by_xpath("//input[@type='text']")
    name.send_keys(your_name)
    next_button = browser1.find_element_by_xpath("//span[@class='appsMaterialWizButtonPaperbuttonContent exportButtonContent']")
    next_button.click()


    arr_question1 = browser1.find_elements_by_class_name("freebirdFormviewerComponentsQuestionRadioChoicesContainer")
    time.sleep(2)
    for radio in arr_question1:
        element = radio.find_elements_by_class_name('docssharedWizToggleLabeledContainer')
        if(to_max_count >= len(element)):
            element[len(element)-1].click()
        else:
            element[to_max_count].click()
    submitt_button1 = browser1.find_element_by_class_name('freebirdFormviewerViewNavigationSubmitButton')
    submitt_button1.click()
    to_max_count = to_max_count + 1