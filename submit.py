# coding=utf-8

import data

import time
from bs4 import BeautifulSoup
from decimal import Decimal, ROUND_HALF_UP


def selenium_submit(url: str, driver):

    print(f"Getting resources from {url} ...")

    driver.get(url)

    start = time.time()

    page = BeautifulSoup(driver.page_source, 'lxml').prettify()
    # print(page)

    print("Got web page, now start filling")
    time.sleep(3)

    # Start filling the form
    q1 = driver.find_element_by_id("q1")
    q1.clear()
    q1.send_keys(data.team_name)

    q2_js = 'document.getElementById("q2_2").click()'
    driver.execute_script(q2_js)

    q3 = driver.find_element_by_id("q3")
    q3.clear()
    q3.send_keys(data.team[0].name)

    q4 = driver.find_element_by_id("q4")
    q4.clear()
    q4.send_keys(data.team[0].qq)

    q5 = driver.find_element_by_id("q5")
    q5.clear()
    q5.send_keys(data.team[0].phone)

    q6 = driver.find_element_by_id("q6")
    q6.clear()
    q6.send_keys(data.team[0].school)

    q7 = driver.find_element_by_id("q7")
    q7.clear()
    q7.send_keys(data.team[0].year)

    q8 = driver.find_element_by_id("q8")
    q8.clear()
    q8.send_keys(data.team[1].name)

    q9 = driver.find_element_by_id("q9")
    q9.clear()
    q9.send_keys(data.team[1].school)

    q10 = driver.find_element_by_id("q10")
    q10.clear()
    q10.send_keys(data.team[1].year)

    q11 = driver.find_element_by_id("q11")
    q11.clear()
    q11.send_keys(data.judges[0].name)

    q12 = driver.find_element_by_id("q12")
    q12.clear()
    q12.send_keys(data.judges[0].qq)

    q13 = driver.find_element_by_id("q13")
    q13.clear()
    q13.send_keys(data.judges[0].phone)

    q14 = driver.find_element_by_id("q14")
    q14.clear()
    q14.send_keys(data.judges[0].resume)

    time.sleep(3)

    print("All filled!")
    time.sleep(3)

    driver.find_element_by_id('submit_button').click()
    print("Click submit button now!")

    print("Registration success")

    driver.quit()
    end = time.time()
    registration_time = Decimal(end - start).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    print(f"It took {registration_time} seconds, now quit")


if __name__ == '__main__':
    print()
