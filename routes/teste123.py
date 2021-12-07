"""Rotas da teste123 SMS."""

import json
from fastapi import APIRouter, Request

teste123_router = APIRouter()


@teste123_router.post("/vendor/teste123/sms/dlr", tags=["teste123"])
async def parse_dlr(request: Request):
    """Parseamento referente aos status de entrega da mensagem retornado pelo fornecedor.

    :return:
        Message (json): Mensagem sobre o retorno
        Code (int): Código referente ao retorno
    """
    body = await request.body()
    payload_str = body.decode("utf-8")
    payload = json.loads(payload_str)

    return {"payload": payload, "success": 200}


@teste123_router.post("/vendor/teste123/sms/response", tags=["teste123"])
async def parse_response(request: Request):
    """Parseamento referente aos status de entrega da mensagem retornado pelo fornecedor.

    :return:
        Message (json): Mensagem sobre o retorno
        Code (int): Código referente ao retorno
    """
    body = await request.body()
    payload_str = body.decode("utf-8")
    payload = json.loads(payload_str)

    return {"payload": payload, "success": 200}