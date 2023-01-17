import platform
so = platform.system()

from selenium import webdriver

def browser():
    if so == "Windows":
        return webdriver.Firefox(executable_path="config/geckodriver.exe")
    elif so == "Linux":
        return webdriver.Firefox()
        