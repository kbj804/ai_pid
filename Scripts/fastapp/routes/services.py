from typing import List
from uuid import uuid4

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.requests import Request

from Scripts.fastapp.common.consts import MAX_API_KEY, MAX_API_WHITELIST
from Scripts.fastapp.database.conn import db
from Scripts.fastapp.database.schema import Users, ApiKeys, ApiWhiteLists
from Scripts.fastapp import models as m
from Scripts.fastapp.errors import exceptions as ex
import string
import secrets

from Scripts.fastapp.models import MessageOk

router = APIRouter(prefix='/services')


@router.get('')
async def get_all_services(request: Request):
    return dict(your_email=request.state.user.email)