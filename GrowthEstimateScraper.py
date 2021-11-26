import numpy as np
import pandas as pd

import urllib.request as urllib2
from bs4 import BeautifulSoup, Tag

import sys

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

verbose = False


def parse_html_table(table):
    n_columns = 0
    n_rows = 0
    column_names = []

    # FIND NUMBER OF ROWS AND COLUMNS
    for row in table.find_all('tr'):

        # DETERMINE NUMBER OF ROWS
        td_tags = row.find_all('td')
        if len(td_tags) > 0:
            n_rows += 1
            if n_columns == 0:
                # DETERMINE NUMBER OF COLUMNS
                n_columns = len(td_tags)

        # HANDLE COLUMN NAMES
        th_tags = row.find_all('th')
        if len(th_tags) > 0 and len(column_names) == 0:
            for th in th_tags:
                column_names.append(th.get_text())

    if 'Invalid Date' in column_names:
        return pd.DataFrame(columns=column_names)

    # CHECKS IF COLUMN ATTRIBUTES ARE VALID
    if len(column_names) > 0 and len(column_names) != n_columns:
        raise Exception("Column titles do not match the number of columns")

    columns = column_names if len(column_names) > 0 else range(0, n_columns)
    df = pd.DataFrame(columns=columns,
                      index=range(0, n_rows))
    row_marker = 0
    for row in table.find_all('tr'):
        column_marker = 0
        columns = row.find_all('td')
        for column in columns:
            df.iat[row_marker, column_marker] = column.get_text()
            column_marker += 1
        if len(columns) > 0:
            row_marker += 1

    # CONVERTS TO FLOAT
    for col in df:
        try:
            df[col] = df[col].astype(float)
        except ValueError:
            pass
    return df

#MAIN CODE TO GET GROWTH RATE
def getLTGrowthRate(stock):
    url = 'https://ca.finance.yahoo.com/quote/{s}/analysts?p={s}'.format(s=stock)
    headers = {'User-Agent': user_agent}

    req = urllib2.Request(url, None, headers)
    response = urllib2.urlopen(req)
    content = response.read()

    soup = BeautifulSoup(content, 'html.parser')
    LTGrowthRate = 0.0
    for table in soup.find_all('table'):
        df = parse_html_table(table)

        if df.columns.values[0] == 'Growth Estimates':
            stk = df[df['Growth Estimates'] == 'Next 5 Years (per annum)'][stock].values[0].replace('%', '')

            LTGrowthRate = stk if stk != 'N/A' else 5.0

    return LTGrowthRate
