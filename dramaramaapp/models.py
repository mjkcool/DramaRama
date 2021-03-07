from django.db import models
from datetime import datetime

# Create your models here.
class Drama(models.Model):
    value = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    channel = models.CharField(max_length=100)
    info_url = models.TextField()

class Survey(models.Model):
    date = models.DateField(blank=True, editable=False)
    age = models.IntegerField(blank=True, null=True)
    GENDER = [('W', '여자'), ('M', '남자')]
    gender = models.CharField(
        blank=True, max_length=2, choices=GENDER,)
    PERSON = [('외향', '외향형'), ('내향', '내향형')]
    personality = models.CharField(max_length=2, choices=PERSON,)
    activity = models.BooleanField()
    job = models.CharField(max_length=100)
    interested = models.TextField()
    school = models.BooleanField()
    work = models.BooleanField()
    ABODE = [('I.C','국내 수도권'), ('I.P', '국내 지방'), ('F','해외')]
    abode = models.CharField(max_length=5, choices=ABODE,)
    siblings = models.IntegerField()
    family = models.IntegerField()
    livealone = models.BooleanField()
    MAJOR = [('이','이과'), ('문','문과')]
    major = models.CharField(max_length=10, choices=MAJOR,)
    ECONOMY_STATUS = [('L','부족함'), ('A','넉넉함'), ('H','부유함')]
    homeeconomy = models.CharField(
        blank=True, max_length=10, choices=ECONOMY_STATUS,)
    havedate = models.BooleanField()
    physicaltrouble = models.NullBooleanField()
    mentaltrouble = models.NullBooleanField()
    prefergenre = models.TextField()
    CHANNEL_TYPE = [('지상파','지상파'), ('케이블','케이블')]
    preferchannel = models.CharField(max_length=10, choices=CHANNEL_TYPE)
    TIME = [('D','6-18시'), ('N','18-6시')]
    watchingtime = models.CharField(max_length=50, choices=TIME)
    DEVICE = [('L','TV 또는 빔 프로젝터'),('M','컴퓨터(데스크탑)'),('S','휴대용 기기(노트북, 휴대폰 등)')]
    used = models.CharField(max_length=10, choices=DEVICE)
    WAY = [('O','본방송'), ('R','재방송'), ('V','다시보기 다운로드(유료 또는 무료)'),
           ('P','다시보기, 연재작(온라인 콘텐츠 플랫폼 ex.NETFLIX, 왓챠)')]
    way = models.CharField(max_length=10, choices=WAY)
    first = models.TextField()
    second = models.TextField()
    third = models.TextField()

class R_Survey(models.Model):
    date = models.DateField(default=datetime.now, editable=False)
    age = models.IntegerField(blank=True, null=True)
    GENDER = [('W', '여자'), ('M', '남자')]
    gender = models.CharField(
        blank=True, max_length=2, choices=GENDER,)
    PERSON = [('외향', '외향형'), ('내향', '내향형')]
    personality = models.CharField(max_length=2, choices=PERSON,)
    activity = models.BooleanField()
    job = models.CharField(max_length=100)
    interested = models.TextField()
    school = models.BooleanField()
    work = models.BooleanField()
    ABODE = [('I.C', '국내 수도권'), ('I.P', '국내 지방'), ('F', '해외')]
    abode = models.CharField(max_length=5, choices=ABODE, )
    siblings = models.IntegerField()
    family = models.IntegerField()
    livealone = models.BooleanField()
    MAJOR = [('이', '이과'), ('문', '문과')]
    major = models.CharField(max_length=10, choices=MAJOR, )
    ECONOMY_STATUS = [('L', '부족함'), ('A', '넉넉함'), ('H', '부유함')]
    homeeconomy = models.CharField(
        blank=True, max_length=10, choices=ECONOMY_STATUS, )
    havedate = models.BooleanField()
    physicaltrouble = models.NullBooleanField()
    mentaltrouble = models.NullBooleanField()
    prefergenre = models.TextField()
    CHANNEL_TYPE = [('지상파', '지상파'), ('케이블', '케이블')]
    preferchannel = models.CharField(max_length=10, choices=CHANNEL_TYPE)
    TIME = [('D', '6-18시'), ('N', '18-6시')]
    watchingtime = models.CharField(max_length=50, choices=TIME)
    DEVICE = [('L', 'TV 또는 빔 프로젝터'), ('M', '컴퓨터(데스크탑)'), ('S', '휴대용 기기(노트북, 휴대폰 등)')]
    used = models.CharField(max_length=10, choices=DEVICE)
    WAY = [('O', '본방송'), ('R', '재방송'), ('V', '다시보기 다운로드(유료 또는 무료)'),
           ('P', '다시보기, 연재작(온라인 콘텐츠 플랫폼 ex.NETFLIX, 왓챠)')]
    way = models.CharField(max_length=10, choices=WAY)
    first = models.TextField()
    second = models.TextField()
    third = models.TextField()