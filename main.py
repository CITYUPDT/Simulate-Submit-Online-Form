# coding=utf-8

import fetch
import data
import submit

import time
from enum import Enum, auto
from selenium import webdriver
import platform


class Registration(Enum):
    test = auto()
    real = auto
    gap = auto()


def check_registration_status() -> Registration:
    now = int(time.time())

    if data.test_start_timestamp < now < data.test_end_timestamp:
        return Registration.test
    elif now > data.real_start_timestamp:
        return Registration.real
    else:
        return Registration.gap


def parse_header() -> dict:
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-HK,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-HK;q=0.6,en-US;q=0.5,ja;q=0.4',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain; charset=UTF-8',
        'Host': 'www.wjx.cn',
        'Origin': 'https://www.wjx.cn',
        'Referer': get_url(),
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
    }

    return headers


def get_url() -> str:
    cases = {
        Registration.test: data.test_url,
        Registration.real: data.real_url,
        Registration.gap: data.real_url,
    }

    status = check_registration_status()
    # print(cases[status])
    return cases[status]


def set_driver():
    # Set driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    print("Setting up driver...")

    driver = None
    if 'Windows' in platform.system():
        driver = webdriver.Chrome(executable_path='venv\chromedriver.exe', options=chrome_options)
    print("Set up driver success!")
    return driver


def main():
    fetch.fetch_info()

    headers = parse_header()
    url = get_url()

    driver = set_driver()

    submit.selenium_submit(url, driver)


if __name__ == '__main__':
    main()
