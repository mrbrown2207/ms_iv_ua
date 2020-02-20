"""Definitions for entire project go here"""

"""Tab Ids"""
ISSUES_TAB = 1
FEATURES_TAB = 2

"""Filter codes"""
ISSUES_ALL = 0
ISSUES_REPORTED = 1
ISSUES_ONGOING = 2
ISSUES_CLOSED = 3

FEATURES_ALL = 4
FEATURES_REQUESTED = 5
FEATURES_ACCEPTED = 6
FEATURES_DECLINED = 7
FEATURES_FINISHED = 8

NO_BOTS = {
    '1 and 1 and 1':'3',
    '1 and 2 and 1':'4',
    '1 and 1 and 2':'4',
    '2 and 2 and 2':'6',
    '2 and 2 and 1':'5',
    '2 and 1 and 1':'4',
    '3 and 3 and 3':'9',
    '3 and 2 and 1':'6',
    '3 and 3 and 2':'8',
    '1 and 1 and 3':'5',
    '2 and 3 and 2':'7',
    '5 and 2 and 1':'8',
    '1 and 0 and 0':'1',
    '0 and 0 and 0':'0',
    '5 and 4 and 0':'9',
    '4 and 1 and 1':'6'
}