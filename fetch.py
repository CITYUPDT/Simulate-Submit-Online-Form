# coding=utf-8

import data

import pandas as pd
import xlrd
from _datetime import datetime
import time


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
pd.set_option('display.max_colwidth', 100)

team_info_file = "test.xlsx"


def fetch_info():
    fetch_basic_info()
    fetch_team_info()
    fetch_judge_info()


def fetch_basic_info():

    basic_info = pd.read_excel(team_info_file, sheet_name=0, header=1)
    # print(f'{basic_info} \n')

    data.test_url = basic_info["测试链接"][0]
    data.test_start_datetime = datetime.strptime(basic_info["测试开始时间"][0], '%Y-%m-%d %H:%M:%S')
    data.test_start_timestamp = int(time.mktime(data.test_start_datetime.timetuple()))
    data.test_end_datetime = datetime.strptime(basic_info["测试结束时间"][0], '%Y-%m-%d %H:%M:%S')
    data.test_end_timestamp = int(time.mktime(data.test_end_datetime.timetuple()))

    data.real_url = basic_info["正式链接"][0]
    data.real_pre_fill_datetime = datetime.strptime(basic_info["开始填表时间"][0], '%Y-%m-%d %H:%M:%S')
    data.real_pre_fill_timestamp = int(time.mktime(data.real_pre_fill_datetime.timetuple()))
    data.real_start_datetime = datetime.strptime(basic_info["报名开始时间"][0], '%Y-%m-%d %H:%M:%S')
    data.real_start_timestamp = int(time.mktime(data.real_start_datetime.timetuple()))

    data.team_name = basic_info["队伍名称"][0]
    data.competition_type = basic_info["比赛项目"][0]


def fetch_team_info():
    team_info = pd.read_excel(team_info_file, sheet_name=1, header=1).fillna(-1).astype(str)
    # print(f'{team_info} \n')

    member_count = team_info["队员姓名"].count()
    for i in range(member_count):
        leader = False

        name = team_info["队员姓名"][i]
        if name == '-1':
            continue

        qq = team_info["QQ"][i].split('.')[0]
        if qq != '-1':
            leader = True

        phone = team_info["手机"][i].split('.')[0]

        school = team_info["学校"][i]

        year = team_info["年级数"][i].split('.')[0]

        member = data.Teammate(name, qq, phone, school, year, leader)
        data.team.append(member)


def fetch_judge_info():
    judge_info = pd.read_excel(team_info_file, sheet_name=2, header=1).astype(str)
    # print(f"{judge_info} \n")

    # This can handle the case that more than one judges
    judge_count = judge_info["评委姓名"].count()
    for i in range(judge_count):
        name = judge_info["评委姓名"][i]
        year = judge_info["评委本科入学年份"][i]
        qq = judge_info["评委QQ"][i].split('.')[0]
        phone = judge_info["评委手机号"][i].split('.')[0]
        resume = judge_info["评委履历"][i]

        judge = data.Judge(name, year, qq, phone, resume)
        data.judges.append(judge)


if __name__ == '__main__':
    fetch_info()
