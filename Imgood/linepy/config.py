# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
import re

class Config(object):
    LINE_HOST_DOMAIN            = 'https://gd2.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_TIMELINE_API           = 'https://gd2.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://gd2.line.naver.jp/mh'
    LINE_OBJECT_URL             = 'https://obs.line-scdn.net/'
    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'

    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'
    LINE_SHOP_QUERY_PATH        = '/SHOP4'
    LINE_LIFF_QUERY_PATH        = '/LIFF1'

    CHANNEL_ID = {
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814',
        'LINE_SERVICES': '1459630796'
    }

    HEADERS = {
        "ANDROIDLITE": {
               "user-agent": "Line/2.17.0",
               "x-line-application": "ANDROIDLITE\t2.17.0\tAndroid OS\t10;SECONDARY"
        },
        "DESKTOPMAC": {
               "user-agent": "Line/10.21.3",
               "x-line-application": "DESKTOPMAC\t7.0.0\tWindows\t10"
        },
        "CHROMEOS": {
              "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50",
              "x-line-application": "CHROMEOS\t2.4.5\tChrome OS\t1"
        },
        "DESKTOPWIN": {
             "user-agent": "Line/7.0.0",
             "x-line-application": "DESKTOPWIN\t7.0.0\tWindows\t10"
        }        
    }

    APP_TYPE    = "CHROMEOS" #CHOOSE YOUR HEADERS
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = 'MR.ANG'
    SYSTEM_VER  = '10.0.0'
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

    def __init__(self):
        #sniff chrome headers and use those instead, because these will get you messagebanned
        self.USER_AGENT = self.HEADERS[self.APP_TYPE]["user-agent"]
        self.APP_NAME = self.HEADERS[self.APP_TYPE]["x-line-application"]
