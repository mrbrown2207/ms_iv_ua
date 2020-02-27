"""Definitions for entire project go here"""

"""Tab Ids"""
TABS = {
    'issues':1,
    'features':2,
}

"""Filter codes"""
FILTERS = {
    'issues_all':0,
    'issues_reported':1,
    'issues_ongoing':2,
    'issues_closed':3,
    'features_all':4,
    'features_requested':5,
    'features_accepted':6, # UA has accepted feature and awaits payment from requester
    'features_working':7, # Requester has paid
    'features_declined':8,
    'features_finished':9,
}

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

DEFAULT_CURRENCY = 'GBP'