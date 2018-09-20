from selenium.webdriver.support.ui import Select
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import time
import csv

try:
    browser = Chrome()
    browser.get("http://student3plus.unsw.edu.au")
    browser.implicitly_wait(10)

    button = browser.find_element_by_id("edit-field-program-career-tid-1")
    button.click()

    dropdown1 = browser.find_element_by_id("edit-field-faculty-tid-offering")
    selector = Select(dropdown1)
    selector.select_by_value("1479")

    dropdown2 = browser.find_element_by_id("edit-field-school-tid-offering")
    selector = Select(dropdown2)
    selector.select_by_value("1991")

    time.sleep(3)

    html = browser.page_source
    soup = BeautifulSoup(html)

    data = []
    table = soup.find('table', attrs={'class': 'course_list'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        print('--=---------=-----------=')
        print(row)
        availability = []
        index = 0
        for col in cols:
            index = index + 1
            result = col.find_all('span', attrs={'class': 'correct'})
            if len(result) > 0:
                availability.append(index-4)
        print(availability)
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    browser.close()

    with open("output.csv", "w", newline='') as f:
        writer = csv.writer(f)
        for row in data:
            if len(row) == 3:
                row.append("Prerequisite: None")
            if len(row) == 4:
                writer.writerow(row)

except Exception:
    print(Exception)
    browser.close()
