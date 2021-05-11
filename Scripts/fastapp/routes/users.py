from typing import List
from uuid import uuid4

import bcrypt
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request
from fastapi.logger import logger

from Scripts.fastapp.common.consts import MAX_API_KEY, MAX_API_WHITELIST
from Scripts.fastapp.database.conn import db
from Scripts.fastapp.database.schema import Users, ApiKeys, ApiWhiteLists
from Scripts.fastapp import models as m
from Scripts.fastapp.errors import exceptions as ex
import string
import secrets

from Scripts.fastapp.models import MessageOk, UserMe

router = APIRouter(prefix='/user')


@router.get('/me', response_model=UserMe)
async def get_me(request: Request):
# async def get_me(request: Request, session: Session = Depends(db.session)): # 세션 가져오는 경우
    user = request.state.user
    user_info = Users.get(id=user.id)
    # 사용 예
    # user_info = Users.filter(id__gt=user.id).order_by("email").all() # 리스트형태 리턴
    # user_info = Users.filter(id__gt=user.id).order_by("email").count()
    # user_info = Users.filter(id__gt=user.id).order_by("email").first()
    # 세션을 가져오면
    # user_info = session.query(Users).filter(User.id > user.id).order_by(Users.email.asc()).count()
    
    return user_info


@router.put('/me')
async def put_me(request: Request):
    ...


@router.delete('/me')
async def delete_me(request: Request):
    ...


@router.get('/apikeys', response_model=List[m.GetApiKeyList])
async def get_api_keys(request: Request):
    """
    API KEY 조회
    :param request:
    :return:
    """
    user = request.state.user
    api_keys = ApiKeys.filter(user_id=user.id).all()
    print("########## api keys ",api_keys)
    return api_keys


@router.post('/apikeys', response_model=m.GetApiKeys)
async def create_api_keys(request: Request, key_info: m.AddApiKey, session: Session = Depends(db.session)):
    """
    API KEY 생성
    :param request:
    :param key_info:
    :param session:
    :return:
    """
    user = request.state.user

    api_keys = ApiKeys.filter(session, user_id=user.id, status='active').count()
    # API KEY 최대 개수 제한
    if api_keys == MAX_API_KEY:
        raise ex.MaxKeyCountEx()

    # 40자리 시크릿 키
    alphabet = string.ascii_letters + string.digits
    s_key = ''.join(secrets.choice(alphabet) for _ in range(40))
    uid = None
    while not uid:
        # from uuid import uuid4 -> 랜덤 값 생성 모듈 -> uuid4의 12자리를 끊어서 uuid 두개를 연결
        uid_candidate = f"{str(uuid4())[:-12]}{str(uuid4())}"
        # 유니크 한지 검사. (테이블에다가 유니크 안걸로 이런식으로 검사 함)
        uid_check = ApiKeys.get(access_key=uid_candidate)
        if not uid_check:
            uid = uid_candidate

    key_info = key_info.dict()
    new_key = ApiKeys.create(session, auto_commit=True, secret_key=s_key, user_id=user.id, access_key=uid, **key_info)
    return new_key


@router.put('/apikeys/{key_id}', response_model=m.GetApiKeyList)
async def update_api_keys(request: Request, key_id: int, key_info: m.AddApiKey):
    """
    API KEY User Memo Update
    :param request:
    :param key_id:
    :param key_info:
    :return:
    """
    user = request.state.user
    key_data = ApiKeys.filter(id=key_id)
    if key_data and key_data.first().user_id == user.id:
        print("1##########################################")
        reet = key_data.update(auto_commit=True, **key_info.dict())
        print(reet.id)
        print("2##########################################")
        return reet
    raise ex.NoKeyMatchEx()


@router.delete('/apikeys/{key_id}')
async def delete_api_keys(request: Request, key_id: int, access_key: str):
    user = request.state.user
    await check_api_owner(user.id, key_id)
    search_by_key = ApiKeys.filter(access_key=access_key)
    if not search_by_key.first():
        raise ex.NoKeyMatchEx()
    search_by_key.delete(auto_commit=True)
    return MessageOk()


@router.get('/apikeys/{key_id}/whitelists', response_model=List[m.GetAPIWhiteLists])
async def get_api_keys(request: Request, key_id: int):
    user = request.state.user
    await check_api_owner(user.id, key_id)
    whitelists = ApiWhiteLists.filter(api_key_id=key_id).all()
    return whitelists


@router.post('/apikeys/{key_id}/whitelists', response_model=m.GetAPIWhiteLists)
async def create_api_keys(request: Request, key_id: int, ip: m.CreateAPIWhiteLists, session: Session = Depends(db.session)):
    user = request.state.user
    await check_api_owner(user.id, key_id)
    # IP 검사
    import ipaddress
    try:
        _ip = ipaddress.ip_address(ip.ip_addr)
    except Exception as e:
        raise ex.InvalidIpEx(ip.ip_addr, e)
    if ApiWhiteLists.filter(api_key_id=key_id).count() == MAX_API_WHITELIST:
        raise ex.MaxWLCountEx()
    ip_dup = ApiWhiteLists.get(api_key_id=key_id, ip_addr=ip.ip_addr)
    if ip_dup:
        return ip_dup
    ip_reg = ApiWhiteLists.create(session=session, auto_commit=True, api_key_id=key_id, ip_addr=ip.ip_addr)
    return ip_reg


@router.delete('/apikeys/{key_id}/whitelists/{list_id}')
async def delete_api_keys(request: Request, key_id: int, list_id: int):
    user = request.state.user
    await check_api_owner(user.id, key_id)
    ApiWhiteLists.filter(id=list_id, api_key_id=key_id).delete()

    return MessageOk()

# key owner와 접속한 사람의 key가 같은지 검사
async def check_api_owner(user_id, key_id):
    api_keys = ApiKeys.get(id=key_id, user_id=user_id)
    if not api_keys:
        raise ex.NoKeyMatchEx()