from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import os
import csv
import pandas as pd
from dramaramaapp.models import *
from datetime import date

from dramaramaapp import main_solution as sol


@method_decorator(csrf_exempt)
def index(request):

    return render(request, 'dramaramaapp/cover.html')

@method_decorator(csrf_exempt)
def form(request):
    request.session['input'] = {}  # init session
    request.session['result'] = {} 
    request.session.modified = True
    return render(request, 'dramaramaapp/form.html')

@method_decorator(csrf_exempt)
def answer(request):
    input_ = request.session.get('input')
    for el in input_.keys():
        input_[el] = ', '.join(input_[el])
    context = {'answer':input_}
    return render(request, 'dramaramaapp/answer.html', context)

@method_decorator(csrf_exempt)
def result(request):
    input_form = dict(request.POST)
    request.session['input'] = input_form

    context = {'Drama':sol.solution(input_form)}

    return render(request, 'dramaramaapp/result.html', context)

@method_decorator(csrf_exempt)
def survey(request):
    return render(request, 'dramaramaapp/survey.html')

@method_decorator(csrf_exempt)
def submitSurvey(request):
    item_names = ['age', 'gender', 'personality', 'activity', 'job', 'interested',
                 'school', 'work', 'abode', 'siblings', 'family', 'livealone', 'major', 'homeeconomy',
                 'havedate', 'physicaltrouble', 'mentaltrouble', 'prefergenre', 'preferchannel',
                 'watchingtime', 'used', 'way', 'first', 'second', 'third']
    items = {}
    for item_name in item_names:
        items[item_name] = request.POST[item_name]

    # data processing
    if items['physicaltrouble'] == "예":
        physicaltrouble_val = True
    elif items['physicaltrouble'] == "아니오":
        physicaltrouble_val = False
    else:
        physicaltrouble_val = None

    if items['mentaltrouble'] == "예":
        mentaltrouble_val = True
    elif items['mentaltrouble'] == "아니오":
        mentaltrouble_val = False
    else:
        mentaltrouble_val = None

    if items['gender'] == '여자':
        GENDER = 'W'
    elif items['gender'] == '남자':
        GENDER = 'M'
    else:
        GENDER = None

    PERSON = {'외향형': '외향', '내향형': '내향'}
    ABODE = {'국내 수도권': 'I.C', '국내 지방': 'I.P', '해외': 'F'}
    MAJOR = {'이과': '이', '문과': '문'}
    if items['homeeconomy'] == '부족함':
        ECONOMY_STATUS = 'L'
    elif items['homeeconomy'] == '넉넉함':
        ECONOMY_STATUS = 'A'
    elif items['homeeconomy'] == '부유함':
        ECONOMY_STATUS = 'H'
    else:
        ECONOMY_STATUS = items['homeeconomy']
    TIME = {'6-18시': 'D', '18-6시': 'N'}
    DEVICE = {'TV 또는 빔 프로젝터': 'L', '컴퓨터(데스크탑)': 'M', '휴대용 기기(노트북, 휴대폰 등)': 'S'}
    WAY = {'본방송': 'O', '재방송': 'R', '다시보기 다운로드(유료 또는 무료)': 'V',
           '다시보기, 연재작(온라인 콘텐츠 플랫폼 ex.NETFLIX, 왓챠)': 'P'}

    # put in database
    R_Survey.objects.create(
        age=items['age'],
        gender=GENDER,
        personality=PERSON[items['personality']],
        activity=True if items['activity'] == "예" else False,
        job=items['job'],
        interested=items['interested'],
        school=True if items['school'] == "예" else False,
        work=True if items['work'] == "예" else False,
        abode=ABODE[items['abode']],
        siblings=items['siblings'],
        family=items['family'],
        livealone=True if items['livealone'] == "예" else False,
        major=MAJOR[items['major']],
        homeeconomy=ECONOMY_STATUS,
        havedate=True if items['havedate'] == "예" else False,
        physicaltrouble=physicaltrouble_val,
        mentaltrouble=mentaltrouble_val,
        prefergenre=items['prefergenre'],
        preferchannel=items['preferchannel'],
        watchingtime=TIME[items['watchingtime']],
        used=DEVICE[items['used']],
        way=WAY[items['way']],
        first=items['first'],
        second=items['second'],
        third=items['third']
    )

    return render(request, 'dramaramaapp/cover.html')