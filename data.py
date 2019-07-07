# coding=utf-8
from dataclasses import dataclass

# --- Basic Info ---
test_url = None
test_start_datetime = None
test_start_timestamp = None
test_end_datetime = None
test_end_timestamp = None

real_url = None
real_pre_fill_time = None
real_start_datetime = None
real_pre_fill_time = None

team_name = None
competition_type = None


# --- Teammates Info ---
@dataclass
class Teammate:
    name: str
    qq: str
    phone: str
    school: str
    year: str
    leader: bool


team = []  # A list of team member


# --- Judge Info ---
@dataclass
class Judge:
    name: str
    qq: str
    phone: str
    resume: str


judges = []
# Normally, only one judge is needed in each team
# But for flexibility, this program is able to handle the case that there are more than one judges

