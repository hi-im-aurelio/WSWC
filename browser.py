import platform
so = platform.system()

from selenium import webdriver


def get_binary_location():
    with open('config/binary_location.coc') as file:
        return file.read().strip()

def browser():
    if so == "Windows":
        return webdriver.Firefox(executable_path="config/geckodriver.exe")
    elif so == "Linux":
        return webdriver.Firefox()


if __name__ == "__main__":
    # added for test compilation
    print(get_binary_location())