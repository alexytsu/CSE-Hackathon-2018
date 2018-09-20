from selenium.webdriver.support.ui import Select
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import time
import csv


def download_course_offerings():
    try:
        # open the website
        browser = Chrome()
        browser.get("http://student3plus.unsw.edu.au")
        browser.implicitly_wait(10)

        # select undergraduate courses
        button = browser.find_element_by_id("edit-field-program-career-tid-1")
        button.click()

        # select the faculty from the dropdown
        dropdown1 = browser.find_element_by_id("edit-field-faculty-tid-offering")
        selector = Select(dropdown1)
        selector.select_by_value("1479")  # Engineering

        # select the school from the dropdown
        dropdown2 = browser.find_element_by_id("edit-field-school-tid-offering")
        selector = Select(dropdown2)
        selector.select_by_value("1991")  # CSE

        # Wait for the table to load before passing the html to Beautiful Soup
        time.sleep(5)
        html = browser.page_source
        soup = BeautifulSoup(html, features="html.parser")

        data = []
        avail = []

        # extract the table of course offerings
        table = soup.find('table', attrs={'class': 'course_list'})
        table_body = table.find('tbody')

        # traverse the rows of the table
        rows = table_body.find_all('tr')
        for row in rows:
            # find the elements in each row
            cols = row.find_all('td')

            # keep track of when each subject is offered
            index = 0
            availability = ['n', 'n', 'n']

            # find when courses are offered
            for col in cols:
                result = col.find_all('span', attrs={'class': 'correct'})
                # if there is the "correct" tick, the course is offered
                if len(result) > 0:
                    availability[index-6] = 'y'
                index = index + 1

            # add this to the list of all availabilities
            avail.append(availability)

            # get the details of a specific subject
            cols = [ele.text.strip() for ele in cols]

            # add this to a list for all subjects
            data.append([ele for ele in cols if ele])

        browser.close()

        # zip course info with when it's offered
        info = zip(data, avail)

        # write the data to csv
        with open("output.csv", "w", newline='') as f:
            writer = csv.writer(f)
            for row in info:
                # some subjects have no requirements
                if len(row[0]) == 3:
                    row[0].append("Prerequisite: None")
                if len(row[0]) == 4:
                    writer.writerow(row[0] + row[1])

    except Exception:
        browser.close()
        raise
