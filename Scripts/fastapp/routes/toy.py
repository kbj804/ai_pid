from typing import List

from fastapi import APIRouter, Depends, FastAPI, File, UploadFile, BackgroundTasks
from sqlalchemy.orm import Session
from starlette.requests import Request

from Scripts.fastapp.common.consts import UPLOAD_DIRECTORY, USING_MODEL_PATH
from Scripts.fastapp.database.conn import db
from Scripts.fastapp import models as m
from Scripts.fastapp.errors import exceptions as ex
from inspect import currentframe as frame

from Scripts.fastapp.database.schema import LeaderBoard

from Scripts.fastapp.common.config import get_logger


import os
router = APIRouter(prefix='/toy')

@router.get('/getLeaderBoard')
async def get_leader_board(request: Request):
    """
    no params\n
    :return\n
    Inzent NB Competition Leader Board
    """
    request.state.inspect = frame()
    result = LeaderBoard.filter(id__gt='0').all()
    
    print("##RESULT##", result)
    # return dict(id=result[0].id, reg_count=result[0].reg_count)
    return result

@router.post('/pushData')
async def input_data(request: Request, session: Session = Depends(db.session)):
    """Input Data"""
    LeaderBoard.create(session, auto_commit=True, team_name="cwh", score=0.01, ip_add= request.state.ip )


@router.post("/uploadFile")
async def upload_submmision(request: Request, background_tasks: BackgroundTasks, team: str, files: List[UploadFile] = File(...) ,session: Session = Depends(db.session)):
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

        LeaderBoard.create(session, auto_commit=True, team_name=team, score=0.01, ip_add= request.state.ip )
        # background_tasks.add_task(cal_score, request = request, team = team, session = session, file=file)

        result = LeaderBoard.filter(id__gt='0').all()
    return result

def cal_score(request, team, session, file):
    pass