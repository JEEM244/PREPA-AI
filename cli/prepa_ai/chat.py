from __future__ import annotations
from .http_client import request_json

class ChatSession:
    def __init__(self,config:dict,base_url:str):
        self.config=config
        self.base_url=base_url
        self.messages=[{"role":"system","content":config["system_prompt"]}]

    def clear(self)->None:
        self.messages=[{"role":"system","content":self.config["system_prompt"]}]

    def send(self,text:str)->str:
        if len(text)>self.config["max_input_chars"]:
            raise ValueError(f"El mensaje supera el límite de {self.config['max_input_chars']} caracteres.")
        # Cuenta el nuevo mensaje dentro del límite de turnos enviado al modelo.
        self._trim_history(max(0,self.config["max_history_turns"]-1))
        self.messages.append({"role":"user","content":text})
        payload={"model":"local-model","messages":self.messages,
                 "temperature":self.config["temperature"],"max_tokens":self.config["max_tokens"],"stream":False}
        try:
            data=request_json(self.base_url+"/v1/chat/completions",payload,
                              timeout=self.config["request_timeout"])
            answer=data["choices"][0]["message"]["content"].strip()
            if not answer: raise ValueError("El modelo devolvió una respuesta vacía.")
        except Exception:
            self.messages.pop()
            raise
        self.messages.append({"role":"assistant","content":answer})
        self._trim_history()
        return answer

    def _trim_history(self,max_turns:int|None=None)->None:
        turns=self.config["max_history_turns"] if max_turns is None else max_turns
        limit=max(0,turns)*2
        if limit==0:
            self.messages=self.messages[:1]
        else:
            self.messages=self.messages[:1]+self.messages[1:][-limit:]
