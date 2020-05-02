from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    button = browser.find_element_by_css_selector(".trollface.btn.btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    print(new_window)

    butt = browser.find_element_by_css_selector("#input_value")
    x = butt.text
    print(x)
    y = calc(x)

    input12 = browser.find_element_by_css_selector("#answer")
    input12.send_keys(y)

    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()