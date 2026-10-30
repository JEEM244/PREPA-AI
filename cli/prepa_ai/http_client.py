from __future__ import annotations
import json
import urllib.request

def request_json(url: str, payload: dict | None = None, timeout: int = 10) -> dict:
    data=None if payload is None else json.dumps(payload,ensure_ascii=False).encode("utf-8")
    headers={"Content-Type":"application/json"} if data is not None else {}
    request=urllib.request.Request(url,data=data,headers=headers)
    with urllib.request.urlopen(request,timeout=timeout) as response:
        result=json.loads(response.read().decode("utf-8"))
    if not isinstance(result,dict):
        raise ValueError("El motor devolvió una respuesta inesperada.")
    return result
