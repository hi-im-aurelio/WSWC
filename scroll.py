from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get('https://www.vivino.com/US-TX/en/brewer-clifton-acin-pinot-noir/w/5087212?year=2015&price_id=21431479')
driver.implicitly_wait(10)
total_page_height = driver.execute_script("return document.body.scrollHeight")
browser_window_height = driver.get_window_size(windowHandle='current')['height']
current_position = driver.execute_script('return window.pageYOffset')

while total_page_height - current_position > browser_window_height:
    driver.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
    current_position = driver.execute_script('return window.pageYOffset')
    sleep(1)  # It is necessary here to give it some time to load the content

mentions_text = driver.find_element(By.XPATH, '//div[@data-testid="mentions"]').text
print(mentions_text)
driver.quit()