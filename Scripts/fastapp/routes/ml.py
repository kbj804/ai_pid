from typing import List

from fastapi import APIRouter, Depends, FastAPI, File, UploadFile
from future.utils import PY2
from h2o.h2o import resume
from sqlalchemy.orm import Session
from starlette.requests import Request

from Scripts.fastapp.common.consts import UPLOAD_DIRECTORY, USING_MODEL_PATH
from Scripts.fastapp.database.conn import db
from Scripts.fastapp.database.schema import Train, Files
from Scripts.fastapp import models as m
from Scripts.fastapp.errors import exceptions as ex
from inspect import currentframe as frame

from Scripts.fastapp.utils.ml.h2o_helper import H2oClass
from Scripts.fastapp.utils.ml.preprocess_train import preprocess, train_save_model, load_ml_model, predict_pid, pushpushbaby

from ast import literal_eval

import os
router = APIRouter(prefix='/ml')
hoo = H2oClass()

@router.get('/getTrainData', response_model=List[m.FeatureToken])
async def show_data(request: Request):
    """
    no params\n
    :return\n
    Train Model
    """
    request.state.inspect = frame()
    result = Train.filter(is_train=False).all()
    train_save_model(result)

    # print("##RESULT##", result)
    # return dict(id=result[0].id, reg_count=result[0].reg_count)
    return result


@router.get('/getPidTest')
async def get_pidpidpid(request: Request, id:int):
    """    
    Train에서 is_train True 인것들 중에
    중복제거하고 file_id로 sum(reg_count)가 0이상이면 File의 is_pid = True
    """
    request.state.inspect = frame()
    result = Train.filter(is_train=True, file_id=id, reg_count__gt= 0).count()  # reg_count가 0이상인게 한개라도 있으면..
    # if result > 0:
    #     info = literal_eval("{'is_pid': True}")
    #     ret = Files.filter(file_id=id)
    #     ret.update(auto_commit=True, **info)

    return result

@router.put('/updateTD')
# async def update_train_data(request:Request, info : m.AddIsTrain):
async def update_train_data(request:Request):
    """
    train데이터 중 학습에 활용된 데이터는 True로 변경
    """
    request.state.inspect = frame()
    result = Train.filter(is_train=False)

    # 여기에서 True로 바꿔주면 됨..
    info = literal_eval("{'is_train': True}") # literal_eval: str -> dict
    print("#################",info)

    ret = result.update(auto_commit=True, **info)
    
    return ret


@router.get('/getLoadML')
async def get_load_ml_md(request: Request):
    """
    no params\n
    :return\n
    Load ML Model
    """
    request.state.inspect = frame()
    # result = Train.filter(y=1).all()
    hoo.load_md(USING_MODEL_PATH)

    result = Files.filter(is_pid=False).all()
    # print("##RESULT##", result)
    # return dict(id=result[0].id, reg_count=result[0].reg_count)
    return result

@router.get('/getPredictFile')
async def get_predict_file_id(request: Request, file_id: int):
    """
    params: file_id\n
    :return\n
    Predict Result
    hoo.predict: List
    ex) [0, 0, 1, 0, 0] / index + 1 = page
    """
    request.state.inspect = frame()
    result = Train.filter(file_id=file_id).order_by("page").all()
    df = preprocess(result)
    hf = hoo.df_to_hf(df)
    hoo.predict(hf)
    
    result_list = [i+1 for  i, value in enumerate(hoo.preds) if value == 1]
    # model = load_ml_model(USING_MODEL_PATH)
    if not result_list:
        return "NO PID"

    return result_list

@router.get('/getPredictPage')
async def get_predict_train_id(request: Request, train_id: int):
    """
    params: train_id(page_id)\n
    :return\n
    Predict Result
    ex) [0] or [1]
    """
    request.state.inspect = frame()
    result = Train.filter(id= train_id).all()
    print("######",result)
    df = preprocess(result)
    hf = hoo.df_to_hf(df)
    hoo.predict(hf)
    
    # model = load_ml_model(USING_MODEL_PATH)

    return hoo.preds

import json
from collections import OrderedDict

@router.get('/xedmresponse', response_model = m.XedmToken)
async def xedm_response_test(request: Request):
    """
    no params \n
    descriptions: Xedm Token Test \n
    return XedmToken: \n
    """
    request.state.inspect = frame()
    docid = "2021050310132101"
    page = ['1','25','33','124']

    file_data = OrderedDict()
    ispid: str = 'T'

    pinfo_data = {"name":"ext:pinfo", "value": ispid }
    pPage_data = {"name":"ext:pPage", "value": ', '.join(page) }

    file_data["attrData"] = {"docId": docid, "attrList":[pinfo_data, pPage_data]}

    return file_data


from Scripts.fastapp.utils.file_module.load_file_manager import loadFileManager
from Scripts.fastapp.utils.preprocess_reg import preprocess_reg

@router.post("/uploadFiles")
async def upload_files_predict_y(request: Request, docid: str, files: List[UploadFile] = File(...) ,session: Session = Depends(db.session)):
    """
    params: docid, file \n
    return: Last File's \n
    return Sample: \n
    "url: api/ml/xedmresponse"의 Response 참조
    """

    file_data = OrderedDict()
    pageList : list = []
    ispid: str = 'F'

    for file in files:
        contents = await file.read()
        print(os.path.join('./', file.filename))
        # with open(os.path.join('./', file.filename), "wb") as fp:
        with open(UPLOAD_DIRECTORY + file.filename, "wb") as fp:
            fp.write(contents)
        f = loadFileManager(UPLOAD_DIRECTORY + file.filename)
        obj = Files.create(session, auto_commit=False, name=f.name, ext=f.ext, ip_add= request.state.ip, doc_id=docid )
        # print(obj.id, f.name, f.ext, f.data)
        
        # Init 
        page = 0
        total_reg_count = 0

        for p in f.data:
            df = preprocess_reg(p["td"])

            page += 1
            total_reg_count += df["reg_count"][0]
            
            if df["reg_count"][0] > 0:
                pageList.append(str(page))

            Train.create(session, auto_commit=True, file_id=obj.id ,y=-1, page=p["page"]+1, text_data=p["td"],
                                                    reg_count=int(df["reg_count"][0]), column1=int(df["col1"][0]), column2=int(df["col2"][0]),
                                                    column3=int(df["col3"][0]),column4=int(df["col4"][0]),column5=int(df["col5"][0]),column6=int(df["col6"][0]),
                                                    column7=int(df["col7"][0]),column8=int(df["col8"][0]),column9=int(df["col9"][0]),column10=int(df["col10"][0])
                        )
        

        page_list = Train.filter(file_id=obj.id).order_by("page").all()
        df = preprocess(page_list)
        hf = hoo.df_to_hf(df)
        hoo.predict(hf)
        
        result_list = [str(p+1) for  p, value in enumerate(hoo.preds) if value == 1]
        # model = load_ml_model(USING_MODEL_PATH)
        if result_list:
            ispid = "T"

            info = literal_eval("{'is_pid': True}") # literal_eval: str -> dict
            ret = Files.filter(id=obj.id)
            ret.update(auto_commit=True, **info)




    pinfo_data = {"name":"ext:pinfo", "value": ispid }
    pPage_data = {"name":"ext:pPage", "value": ', '.join(result_list) }

    file_data["attrData"] = {"docId": docid, "attrList":[pinfo_data, pPage_data]}
    print(file_data)
    res = pushpushbaby(file_data)

    # 마지막 파일 f.data
    return str(res.text)