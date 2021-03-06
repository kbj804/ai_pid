from typing import List

from fastapi import APIRouter, Depends, FastAPI, File, UploadFile, BackgroundTasks
from future.utils import PY2
from sqlalchemy.orm import Session
from starlette.requests import Request

from Scripts.fastapp.common.consts import UPLOAD_DIRECTORY, USING_MODEL_PATH
from Scripts.fastapp.database.conn import db
from Scripts.fastapp.database.schema import Train, Files
from Scripts.fastapp import models as m
from Scripts.fastapp.errors import exceptions as ex
from inspect import currentframe as frame

from Scripts.fastapp.utils.ml.preprocess_train import preprocess, xedm_post, connect_session

from Scripts.fastapp.common.config import get_logger

import json
from collections import OrderedDict

from ast import literal_eval

import os
router = APIRouter(prefix='/xedm')
logger = get_logger()

# hoo = H2oClass()

@router.get('/loadml')
async def load_ml_for_xedm(request: Request):
    """
    no params\n
    :return\n
    Load ML Model
    """
    request.state.inspect = frame()
    hoo.load_md(USING_MODEL_PATH)
    if not hoo.model:
        raise ex.XedmLoadFailEx()

    return m.MessageOk()

@router.get('/session')
async def connect_xedm_session(request: Request):
    """
    no params\n
    :return\n
    Connect session
    """
    request.state.inspect = frame()
    res = connect_session()
    logger.info(res)
    if not res:
        raise ex.XedmLoadFailEx()

    return res


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


def predict_using_h2o(request, docid, sid, session, file):
    print("## START PREDICT ON H2O")
    file_data = OrderedDict()
    pageList : list = []
    ispid: str = 'F'

    f = loadFileManager(UPLOAD_DIRECTORY + file.filename)
    
    if not f.data:
        raise ex.FileExtEx(f.name)

    obj = Files.create(session, auto_commit=False, name=f.name, ext=f.ext, ip_add= request.state.ip, doc_id=docid )
    # print(obj.id, f.name, f.ext, f.data)
    
    # Init 
    page = 0
    total_reg_count = 0
    logger.info(f.data)
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

    # ?????? ????????? ?????? ?????? ??????
    if not hoo.model:
        hoo.load_md(USING_MODEL_PATH)
    hoo.predict(hf)

    result_list = [str(p+1) for  p, value in enumerate(hoo.preds) if value == 1]
    # model = load_ml_model(USING_MODEL_PATH)
    if result_list or total_reg_count > 0:
        ispid = "T"

        info = literal_eval("{'is_pid': True}") # literal_eval: str -> dict
        ret = Files.filter(id=obj.id)
        ret.update(auto_commit=True, **info)


    pinfo_data = {"name":"ext:pinfo", "value": ispid }
    pPage_data = {"name":"ext:pPage", "value": ', '.join(result_list) }

    file_data["attrData"] = {"docId": docid, "attrList":[pinfo_data, pPage_data]}
    print(file_data)
    res = xedm_post(file_data, sid)
    print(res.text)



@router.post("/uploadFiles")
async def upload_files_predict_y(request: Request, background_tasks: BackgroundTasks,docid: str, sid: str, files: List[UploadFile] = File(...) ,session: Session = Depends(db.session)):
    """
    params: docid, sid(session id) file \n
    return: Last File's \n
    return Sample: \n
    "OK"
    """
    if not files:
        raise ex.XedmUploadFailEx()
    for file in files:
        contents = await file.read()
        print(os.path.join('./', file.filename))
        # with open(os.path.join('./', file.filename), "wb") as fp:
        with open(UPLOAD_DIRECTORY + file.filename, "wb") as fp:
            fp.write(contents)

        background_tasks.add_task(predict_using_h2o, request = request, docid=docid, sid = sid, session = session, file=file)
    return m.MessageOk()
 
