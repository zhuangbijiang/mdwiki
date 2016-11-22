import os,sys
from celery import Celery
# append xbysite package to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

import logging

VERSION='0.0.1'

APP_NAME = "xbynet平台"
APP_ICON = "/static/assets/images/logo.png"
APP_START_YEAR='2014'
#define the neccery dir
BASE_DIR=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
DATA_DIR=os.path.join(BASE_DIR,'data')
PAGE_DIR=os.path.join(DATA_DIR,'pages')
DOWNLOAD_URL_PREFIX='/data/upload/'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
if not os.path.exists(PAGE_DIR):
    os.makedirs(PAGE_DIR)

###########################
# Flask Config
###########################
DEBUG=True
SECRET_KEY='\xe0N\rl\x8f\xe3\x13\xa6\xdd\r\xea\xd1\x03\x9f+\x1f3\xa3\x18\x1eia\xa2\xbf'
# Extract and use X-Forwarded-For/X-Forwarded-Proto headers?
ENABLE_PROXY_FIX = False
#max upload size 100MB
MAX_CONTENT_LENGTH=1024*1024*100

###########################
# Logging config File Path
###########################
LOG_CFG_FILE=os.path.join(BASE_DIR,'logging.json')
LOG_MAIL_RECIEVER="xbynet@outlook.com"

###########################
# mail config
###########################
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 994
MAIL_USE_SSL = True
MAIL_USERNAME = 'xbynet@163.com'
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD','123')
MAIL_DEFAULT_SENDER = 'xbynet<xbynet@163.com>'

###########################
# SQLAchemy config
###########################
SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(BASE_DIR,'app.db')
#SQLALCHEMY_DATABASE_URI='mysql://root:1234@localhost/xbysite'
SQLALCHEMY_ECHO= True if DEBUG else False
SQLALCHEMY_TRACK_MODIFICATIONS=True if DEBUG else False
#SQLALCHEMY_POOL_SIZE=10
#SQLALCHEMY_POOL_TIMEOUT=60
#SQLALCHEMY_POOL_RECYCLE=2*60*60
#SQLALCHEMY_MAX_OVERFLOW=50

###########################
# Flask-Cache config
###########################
CACHE_TYPE='redis' if not DEBUG else 'null'  #null,simple,memcached,redis,filesystem
CACHE_DEFAULT_TIMEOUT= 1 if DEBUG else 3*60*60
CACHE_KEY_PREFIX='xbysite_'
#CACHE_REDIS_HOST='127.0.0.1'
#CACHE_REDIS_PORT='6379'
#CACHE_REDIS_PASSWORD=''
#CACHE_REDIS_DB=1 #0
CACHE_REDIS_URL='redis://localhost:6379/1' #redis://username:password@localhost:6379/0

###########################
# Flask-WTF config
###########################

###########################
# flask-babel config
###########################
BABEL_DEFAULT_LOCALE = 'zh'
# Your application default translation path
BABEL_DEFAULT_FOLDER = 'translations'
# The allowed translation for you app
LANGUAGES = {
    #'en': {'flag': 'us', 'name': 'English'},
    # 'fr': {'flag': 'fr', 'name': 'French'},
     'zh': {'flag': 'cn', 'name': 'Chinese'},
}

###########################
# Celery config
###########################
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND='redis://localhost/0'
#CELERY_TASK_SERIALIZER='json'
#CELERY_ACCEPT_CONTENT=['json']
#CELERY_RESULT_SERIALIZER='json'
CELERY_TIMEZONE='Asia/Shanghai'
#CELERY_TASK_PUBLISH_RETRY=3
'''CELERY_TASK_PUBLISH_RETRY_POLICY={
    'max_retries': 3, #默认3次，0 or None代表一直重试
    'interval_start': 0,
    'interval_step': 0.2,
    'interval_max': 0.2,
}'''
#周期性任务定义:
'''CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
         'task': 'proj.tasks.add',
         'schedule': timedelta(seconds=30),#'schedule': crontab(hour=7, minute=30, day_of_week=1),
         'args': (16, 16)
    },
}'''



###########################
# Flask-Security config
###########################
SECURITY_PASSWORD_HASH='sha512_crypt' #bcrypt, sha512_crypt, or pbkdf2_sha512
SECURITY_PASSWORD_SALT=SECRET_KEY #default None
SECURITY_EMAIL_SENDER=MAIL_DEFAULT_SENDER
SECURITY_LOGIN_URL='/login'
SECURITY_LOGOUT_URL='/logout'
#SECURITY_REGISTER_URL='/register'
#SECURITY_RESET_URL='/reset'
#SECURITY_CHANGE_URL='/change'
#SECURITY_CONFIRM_URL='/confirm'
SECURITY_POST_LOGIN_VIEW='/'
SECURITY_POST_LOGOUT_VIEW='/'

#SECURITY_REGISTERABLE=True 是否允许用户注册。默认为False
#SECURITY_SEND_REGISTER_EMAIL=True #用户注册时是否发送邮件
#SECURITY_CONFIRMABLE=True #用户注册时是否需要确认邮件

#SECURITY_RECOVERABLE	是否允许密码重置，默认为False
SECURITY_TRACKABLE=True #默认为False，是否需要用户登录统计的相关信息。如果设为True，用户模型需要添加字段
SECURITY_CHANGEABLE=True #是否允许密码修改，默认为False。如果为True，那么交由SECURITY_CHANGE_URL处理。
#SECURITY_EMAIL_SUBJECT_REGISTER	注册确认邮件的主题。
#SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE
#SECURITY_EMAIL_SUBJECT_PASSWORD_RESET
#SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE
#SECURITY_EMAIL_SUBJECT_CONFIRM
#SECURITY_SEND_PASSWORD_CHANGE_EMAIL=True
#SECURITY_SEND_PASSWORD_RESET_NOTICE_EMAIL=True
#SECURITY_CONFIRM_EMAIL_WITHIN	确认邮件链接失效时间，默认5 days.
#SECURITY_RESET_PASSWORD_WITHIN	密码重置邮件链接失效时间，默认5 days.
#SECURITY_DEFAULT_REMEMBER_ME	默认为False，是否允许记住我功能。

