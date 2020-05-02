from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element_by_css_selector("#treasure")
    x = x_element1.get_attribute("valuex")
    print(x)
    x = int(x)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    element_input = browser.find_element_by_css_selector("#answer")
    element_input.send_keys(y)

    element_input = browser.find_element_by_css_selector("#answer")
    element_input.send_keys(y)

    button = browser.find_element_by_css_selector("#robotCheckbox")
    button.click()

    button1 = browser.find_element_by_css_selector("#robotsRule")
    button1.click()

    button2 = browser.find_element_by_css_selector(".btn.btn-default")
    button2.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()