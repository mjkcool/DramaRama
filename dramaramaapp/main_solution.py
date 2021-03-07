import operator
from random import randrange
import random
import pandas as pd
import csv
import sqlite3
import warnings
warnings.filterwarnings("ignore", 'This pattern has match groups')


weight_list = {}  # weight list

def process_weight(drama_code, first, second, third):
    weight = 2  # 가중치
    for step in [first, second, third]:  # type(step) == list
        if not step: continue
        step = list(filter(lambda e: e != '', step))  # 공백 값 제거
        for elem in step:  # type(elem) == str
            elem = elem.replace(' ', '')  # 글자의 공백제거
            if elem in list(drama_code):
                weight_list[drama_code[drama_code == elem].index[0]] += weight
        weight /= 2


def solution(input_data):

    # Read form data
    # form_df = pd.read_csv('./dramaramaapp/static/data/formdata.csv')
    # form_df.drop(['date'], axis='columns', inplace=True)
    # form_df = form_df.fillna('')  # NaN값 제거

    # DB Connection
    # Read survey data
    conn = sqlite3.connect('./db.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM dramaramaapp_survey")
    rows = cur.fetchall()
    cols = [column[0] for column in cur.description]
    form_df = pd.DataFrame.from_records(data=rows, columns=cols)
    cur.close()
    # Read drama data
    cur = conn.cursor()
    cur.execute("SELECT * FROM dramaramaapp_drama")
    rows = cur.fetchall()
    cols = [column[0] for column in cur.description]
    drama_df = pd.DataFrame.from_records(data=rows, columns=cols)
    cur.close()
    conn.close()

    form_df.drop(['date'], axis='columns', inplace=True)
    form_df.drop(['id'], axis='columns', inplace=True) #inplace=True -> 덮어쓰기
    form_df = form_df.fillna('')  # NaN값 제거

    # Column name list
    col_names = list(form_df)

    # drama code
    data = list(drama_df['value'])
    drama_code = pd.Series(data, index=list(drama_df['id'].astype(str))) # key: id

    for idx in list(drama_code.index):  # Initialize weight list
        weight_list[idx] = 0

    weight_df = pd.DataFrame()  # temp repository

    for col in col_names:  # turn all cols in input data
        if col in input_data.keys():  # check there's it
            if type(input_data[col]) == int:
                match = form_df[col] == input_data[col]
                weight_df = form_df[match]
            else:
                for ele in input_data[col]:  # turn all cols in list
                    match = (form_df[col].astype(str)).str.contains(ele)
                    weight_df = pd.concat([weight_df, form_df[match]])

            first = list(weight_df['first'])
            second = list(weight_df['second'])
            third = list(weight_df['third'])

            process_weight(drama_code, first, second, third)  # compute weight
            weight_df = pd.DataFrame()  # Initialize

    weight_list_items = list(weight_list.items())
    random.shuffle(weight_list_items) #리스트 섞기
    suffled_weight_list = dict(weight_list_items)
    #섞인 리스트 정리
    sorted_weight = sorted(suffled_weight_list.items(), key=operator.itemgetter(1), reverse=True)  # form: tuples in list
    drama_obj = drama_df[drama_df['id'].astype(str) == sorted_weight[randrange(3)][0]]

    return dict(drama_obj.iloc[0]) #행을 딕셔너리로