from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response
from starlette.responses import JSONResponse


from starlette.requests import Request
from inspect import currentframe as frame

from Scripts.fastapp.database.conn import db
from Scripts.fastapp.database.schema import Users

router = APIRouter()


@router.get("/")
async def index(request: Request):
# async def index(session: Session = Depends(db.session),):
    """
    ELB 상태 체크용 API
    :return:
    """
    # 방법1
    # user = Users(status='active', name="KBJ")
    # session.add(user)
    # session.commit()

    # 방법2
    # Users().create(session, auto_commit=True, name="boungjin")
    print("### State User ####")
    print("state.user", request.state.user)
    print("state.inspect", frame())
    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})")


@router.get("/test")
async def test(request: Request):
    """
    ELB 상태 체크용 API
    :return:
    """
    print("state.user", request.state.user)
    # try:
    #     a = 1/0
    # except Exception as e:
    #     # 여기서 이런식으로 inspect를 넣어주지 않으면 오류가 뭔지 알 수 없음 "UNKKOWN"
    #     request.state.inspect = frame()
    #     raise e
    current_time = datetime.utcnow()
    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')})\n {request.state.user}")
    return Response(f"Notification {request.state.user}")


@router.get("/vuetest")
async def vuetest(request: Request):
    current_time = datetime.utcnow()
    return JSONResponse(status_code=400, content=dict(msg="NOT_SUPPORTED"))