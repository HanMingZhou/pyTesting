# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    driver = webdriver.Chrome()
    driver.get("https://www.bing.com")

    ## 阻塞主线程
    driver.implicitly_wait(1000)








# See PyCharm help at https://www.jetbrains.com/help/pycharm/
