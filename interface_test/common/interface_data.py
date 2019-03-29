#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def primaryAssess():
    datas = {
        "nextPage": "1",
        "pageLimit": "14",
        "cnd": {
            "flag": "0",
            "fileNumber": "",
            "name": "",
            "concatMethod": "",
            "idNo": "",
            "faceTrialName": "",
            "currentHandler": "",
            "stime": "",
            "etime": "",
            "addressDetail": "",
            "jobAddress": "",
            "guarantyAddress": ""
        }
    }
    return datas