# **[WARNINGS] Don't run this file.
DRAMADATA_DIR = 'dramaramaapp/static/data/dramadata.csv'
with open(DRAMADATA_DIR, newline='', encoding='utf-8') as drama_csv:
    reader = csv.DictReader(drama_csv)
    for row in reader:
        Drama.objects.create(
            value=row['value'],
            title=row['title'],
            channel=row['channel'],
            info_url=row['information']
        )

FORMDATA_DIR = 'dramaramaapp/static/data/formdata.csv'
with open(FORMDATA_DIR, newline='', encoding='utf-8') as form_csv:
    reader = csv.DictReader(form_csv)
    for row in reader:
        date_list = row['date'].split('. ')
        if row['physicaltrouble'] == "예":
            physicaltrouble_val = True
        elif row['physicaltrouble'] == "아니오":
            physicaltrouble_val = False
        else:
            physicaltrouble_val = None

        if row['mentaltrouble'] == "예":
            mentaltrouble_val = True
        elif row['mentaltrouble'] == "아니오":
            mentaltrouble_val = False
        else:
            mentaltrouble_val = None

        if row['gender'] == '여자':
            GENDER = 'W'
        elif row['gender'] == '남자':
            GENDER = 'M'
        else:
            GENDER = None

        PERSON = {'외향형': '외향', '내향형': '내향'}
        ABODE = {'국내 수도권': 'I.C', '국내 지방': 'I.P', '해외': 'F'}
        MAJOR = {'이과': '이', '문과': '문'}
        if row['homeeconomy'] == '부족함':
            ECONOMY_STATUS = 'L'
        elif row['homeeconomy'] == '넉넉함':
            ECONOMY_STATUS = 'A'
        elif row['homeeconomy'] == '부유함':
            ECONOMY_STATUS = 'H'
        else:
            ECONOMY_STATUS = row['homeeconomy']
        TIME = {'6-18시': 'D', '18-6시': 'N'}
        DEVICE = {'TV 또는 빔 프로젝터': 'L', '컴퓨터(데스크탑)': 'M', '휴대용 기기(노트북, 휴대폰 등)': 'S'}
        WAY = {'본방송': 'O', '재방송': 'R', '다시보기 다운로드(유료 또는 무료)': 'V',
               '다시보기, 연재작(온라인 콘텐츠 플랫폼 ex.NETFLIX, 왓챠)': 'P'}

        Survey.objects.create(
            date=date(int(date_list[0]), int(date_list[1]), int(date_list[2])),
            age=row['age'],
            gender=GENDER,
            personality=PERSON[row['personality']],
            activity=True if row['activity'] == "예" else False,
            job=row['job'],
            interested=row['interested'],
            school=True if row['school'] == "예" else False,
            work=True if row['work'] == "예" else False,
            abode=ABODE[row['abode']],
            siblings=row['siblings'],
            family=row['family'],
            livealone=True if row['livealone'] == "예" else False,
            major=MAJOR[row['major']],
            homeeconomy=ECONOMY_STATUS,
            havedate=True if row['havedate'] == "예" else False,
            physicaltrouble=physicaltrouble_val,
            mentaltrouble=mentaltrouble_val,
            prefergenre=row['prefergenre'],
            preferchannel=row['preferchannel'],
            watchingtime=TIME[row['watchingtime']],
            used=DEVICE[row['used']],
            way=WAY[row['way']],
            first=row['first'],
            second=row['second'],
            third=row['third']
        )