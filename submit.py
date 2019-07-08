# coding=utf-8

import data
import fetch

import time
from datetime import datetime
from bs4 import BeautifulSoup
from decimal import Decimal, ROUND_HALF_UP


def selenium_submit(url: str, driver):

    print(f"{fetch.current_time()}Getting web page source from {url} ...")

    driver.get(url)

    start = time.time()

    # Registration web page source code
    page = BeautifulSoup(driver.page_source, 'lxml').prettify()
    # print(page)

    print(f"{fetch.current_time()}Got source! \n")

    print(f'{fetch.current_time()}Now start filling...')
    # TODO: (Modify) Start filling the form
    q1 = driver.find_element_by_id("q1")
    q1.clear()
    q1.send_keys(data.team_name)

    team = data.team
    teammate_no: int = len(team)
    q_no: int = 2

    # 第2-11题是队长&副队长
    for i in range(2):
        q_name = driver.find_element_by_id(f"q{q_no}")
        q_name.clear()
        q_name.send_keys(team[i].name)
        q_no = q_no + 1

        q_qq = driver.find_element_by_id(f"q{q_no}")
        q_qq.clear()
        q_qq.send_keys(team[i].qq)
        q_no = q_no + 1

        q_phone = driver.find_element_by_id(f"q{q_no}")
        q_phone.clear()
        q_phone.send_keys(team[i].phone)
        q_no = q_no + 1

        q_school = driver.find_element_by_id(f"q{q_no}")
        q_school.clear()
        q_school.send_keys(team[i].school)
        q_no = q_no + 1

        q_year = driver.find_element_by_id(f"q{q_no}")
        q_year.clear()
        q_year.send_keys(team[i].year)
        q_no = q_no + 1

        time.sleep(1)

    # 第12-29题是队员3-8
    for i in range(teammate_no-2):
        i = i + 2

        if team[i].name != '-1':
            q_name = driver.find_element_by_id(f"q{q_no}")
            q_name.clear()
            q_name.send_keys(team[i].name)
            q_no = q_no + 1

            q_school = driver.find_element_by_id(f"q{q_no}")
            q_school.clear()
            q_school.send_keys(team[i].school)
            q_no = q_no + 1

            q_year = driver.find_element_by_id(f"q{q_no}")
            q_year.clear()
            q_year.send_keys(team[i].year)
            q_no = q_no + 1

            time.sleep(1)

    q30_1_js = 'document.getElementById("q30_1").checked = true'
    driver.execute_script(q30_1_js)

    q30_2_js = 'document.getElementById("q30_2").checked = true'
    driver.execute_script(q30_2_js)

    time.sleep(1)

    q31 = driver.find_element_by_id("q31")
    q31.clear()
    q31.send_keys(data.judges[0].name)

    q32 = driver.find_element_by_id("q32")
    q32.clear()
    q32.send_keys(data.judges[0].year)

    q33 = driver.find_element_by_id("q33")
    q33.clear()
    q33.send_keys(data.judges[0].qq)

    q34 = driver.find_element_by_id("q34")
    q34.clear()
    q34.send_keys(data.judges[0].phone)

    q35 = driver.find_element_by_id("q35")
    q35.clear()
    q35.send_keys(data.judges[0].resume)

    print(f"{fetch.current_time()}All filled! \n")

    # Fill the form first
    # Wait until submit time
    wait_until_submit(driver)

    driver.quit()
    end = time.time()
    registration_time = Decimal(end - start).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
    print(f"{fetch.current_time()}It took {registration_time} seconds, now quit!")


def wait_until_submit(driver):
    now = int(time.time())
    waiting = data.real_start_timestamp - now
    if now < data.real_start_timestamp:
        print(f"{fetch.current_time()}Please wait {waiting} seconds until {data.real_start_datetime}...")

    while int(time.time()) < data.real_start_timestamp:
        time.sleep(0.1)

    print(f"{fetch.current_time()}Click submit button now!\n")
    driver.find_element_by_id('submit_button').click()

    reminder = f"{fetch.current_time()}Registration form is submitted!"

    print(f"{reminder}")


if __name__ == '__main__':
    print(datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S:%M'))
