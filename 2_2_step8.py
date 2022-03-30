import os 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
#    browser = webdriver.Firefox()
    browser.get(link)
    
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Ivanov")
    
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Ivan@mail.ru")
    
    
    
    
    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname('2_2_step8.py'))  

    file_name = "file.txt"

    # добавляем к этому пути имя файла 
    file_path = os.path.join(current_dir, file_name)  

    element = browser.find_element(By.ID, "file")

    print(current_dir)
    print(file_path) 

    element.send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
