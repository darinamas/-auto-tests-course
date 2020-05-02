from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element_by_css_selector("#num1")
    x1 = int(x_element1.text)
    x_element2 = browser.find_element_by_css_selector("#num2")
    x2 = int(x_element2.text)
    y = str(x1+x2)
    print(y)

    select = browser.find_element_by_tag_name("select").click()

    list1 = browser.find_element_by_css_selector("[value='" + y + "']").click()

    button2 = browser.find_element_by_css_selector(".btn.btn-default")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

