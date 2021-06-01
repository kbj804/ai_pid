import pandas as pd
from Scripts.fastapp.database.schema import Train, Files
# from Scripts.fastapp.database.conn import db
# from sqlalchemy.orm import Session
# from fastapi import  Depends

## 임시
from Scripts.fastapp.common.consts import H2O_MODEL_PATH
from Scripts.fastapp.utils.ml.h2o_helper import H2oClass
from ast import literal_eval

import requests
import json

def preprocess(results:list):
    """
    학습용 Data Frame 생성
    """
    data: list = []
    columns = ['id','reg_count','col1','col2','col3','col4','col5','col6','col7','col8','col9','col10']
    for _, r in enumerate(results):
        a=[]
        a.append(r.id)
        a.append(r.reg_count)

        for i in range(1, 11):
            a.append(eval(f"r.column{i}"))

        # a.append(r.column1)
        # a.append(r.column2)
        # a.append(r.column3)
        # a.append(r.column4)
        # a.append(r.column5)
        # a.append(r.column6)
        # a.append(r.column7)
        # a.append(r.column8)
        # a.append(r.column9)
        # a.append(r.column10)
        # a.append(r.y)
        data.append(a)
    
    print(pd.DataFrame(data, columns=columns))
    return pd.DataFrame(data, columns=columns)


def train_save_model(train_data: list):
    df = preprocess(train_data)
    hhh = H2oClass()
    hf = hhh.df_to_hf(df)
    hhh.split_data(hf)
    ml = hhh.train_model()
    hhh.save_md(ml)

def load_ml_model(model_path):
    h = H2oClass()
    model_ = h.load_md(model_path)

    return model_

def predict_pid(data, model):
    df = preprocess(data)
    h = H2oClass()
    d = h.df_to_hf(df)
    p = model.predict(d)


def xedm_post(data, sid):
    print("####### PUSH PUSH POST ######")
    # url = f"http://183.111.96.15:7086/xedrm/json/updateDocEx?sid={sid}"
    url = f"http://192.168.21.29:9080/xedrm/json/updateDocEx?sid={sid}"
    jsondata = json.dumps(data, indent=4)
    headers = {'Content-Type': 'application/json;'}
    res = requests.post(url, headers= headers,data = jsondata)
    print(res)
    print(jsondata)
    print("####### PUSH DONE ######")
    return res

def connect_session():
    print("####### Connection Xedm Session ######")
    url = 'http://183.111.96.15:7086/xedrm/json/login?isAgent=True&lang=ko&userId=Qmhp/4rwH78=&mode=jwt'

    res = requests.get(url)
    res = json.loads(res.text)
    session = res['list'][0]['xedmSession']

    return session


# from collections import OrderedDict

# file_data = OrderedDict()
# pinfo_data = {"name":"ext:pinfo", "value": "T" }
# pPage_data = {"name":"ext:pPage", "value": "" }

# file_data["attrData"] = {"docId": "2021050310132101", "attrList":[pinfo_data, pPage_data]}

sres = connect_session()
# sres_d = json.loads(sres.text)


# res = pushpushbaby(file_data)
# print(res.text)
