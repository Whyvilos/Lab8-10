from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from array import *

def main():
    
    driver = webdriver.Chrome()
    f = open('list.txt', 'r')
    
    sites = f.read().splitlines()
    
    f.close()
    for x in sites:
        print(x) 
    sites2 = sites

    for x in sites:
        driver.get(x)
        TAG_A = driver.find_elements_by_tag_name('a')
        for i in TAG_A:
            for y in sites:
                if i.get_attribute('href') == y:
                    sites2.remove(y)

    f = open('result.txt', 'w')

    print('После обработки')

    for x in sites2: 
        print(x)
        f.write(x + '\n')
    f.close()

if __name__ == "__main__":
    main()
